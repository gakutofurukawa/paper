#!/usr/bin/env python3
"""
参考文献自動生成スクリプト
refs/内のPDFからDOI抽出 → BibTeX生成 → src/references.bibに統合
"""

import os
import re
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, List, Set

def extract_doi_from_pdf(pdf_path: Path) -> Optional[str]:
    """PDFからDOIを抽出"""
    try:
        with open(pdf_path, 'rb') as f:
            # 最初の50KBだけ読む（DOIは通常論文の最初にある）
            content = f.read(50000).decode('utf-8', errors='ignore')
        
        # DOIパターン: 10.xxxx/xxxxx
        doi_pattern = r'10\.\d{4,9}/[-._;()/:A-Z0-9]+'
        match = re.search(doi_pattern, content, re.IGNORECASE)
        
        if match:
            return match.group(0)
        
        # ファイル名からも試す
        filename_match = re.search(doi_pattern, pdf_path.stem, re.IGNORECASE)
        if filename_match:
            return filename_match.group(0)
            
    except Exception as e:
        print(f"   ⚠️  読み込みエラー: {e}")
    
    return None

def get_bibtex_from_doi(doi: str) -> Optional[str]:
    """DOIからBibTeXを取得（CrossRef API）"""
    try:
        url = f"https://doi.org/{doi}"
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/x-bibtex; charset=utf-8")
        
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                return response.read().decode('utf-8').strip()
    except urllib.error.HTTPError as e:
        print(f"   ⚠️  HTTP Error {e.code}: {doi}")
    except urllib.error.URLError as e:
        print(f"   ⚠️  URL Error: {e.reason}")
    except Exception as e:
        print(f"   ⚠️  API呼び出しエラー: {e}")
    
    return None

def extract_citation_key(bibtex: str) -> Optional[str]:
    """BibTeXからcitation keyを抽出"""
    match = re.search(r'@\w+\{([^,]+),', bibtex)
    return match.group(1) if match else None

def load_existing_keys(bib_file: Path) -> Set[str]:
    """既存のreferences.bibからcitation keyを抽出"""
    keys = set()
    if bib_file.exists():
        try:
            with open(bib_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # @article{KEY, や @inproceedings{KEY, などを抽出
            keys = set(re.findall(r'@\w+\{([^,]+),', content))
        except Exception as e:
            print(f"⚠️  既存ファイル読み込みエラー: {e}")
    return keys

def main():
    """メイン処理"""
    print("📚 参考文献を自動生成中...\n")
    
    # パス設定
    refs_dir = Path("refs")
    bib_file = Path("src/references.bib")
    
    # refs/ディレクトリの確認
    if not refs_dir.exists():
        print("⚠️  refs/ ディレクトリが見つかりません")
        print("💡 作成します: refs/")
        refs_dir.mkdir(exist_ok=True)
        print("✅ refs/ ディレクトリを作成しました")
        print("📝 PDFファイルを refs/ に配置してください\n")
        return
    
    # PDFファイルを検索
    pdf_files = list(refs_dir.glob("**/*.pdf"))
    
    if not pdf_files:
        print("⚠️  refs/ 内にPDFファイルが見つかりません")
        print("📝 PDFファイルを refs/ に配置してください\n")
        return
    
    print(f"📄 {len(pdf_files)}個のPDFを検出\n")
    
    # 既存のcitation keyを取得
    existing_keys = load_existing_keys(bib_file)
    if existing_keys:
        print(f"📖 既存の参考文献: {len(existing_keys)}件\n")
    
    # 新規エントリを収集
    new_entries: List[str] = []
    skipped = 0
    no_doi = 0
    
    for pdf_file in pdf_files:
        print(f"📄 処理中: {pdf_file.name}")
        
        # DOI抽出
        doi = extract_doi_from_pdf(pdf_file)
        if not doi:
            print(f"   ⚠️  DOIが見つかりません")
            no_doi += 1
            continue
        
        print(f"   🔍 DOI検出: {doi}")
        
        # BibTeX取得
        bibtex = get_bibtex_from_doi(doi)
        if not bibtex:
            print(f"   ❌ BibTeX取得失敗")
            continue
        
        # 重複チェック
        citation_key = extract_citation_key(bibtex)
        if citation_key and citation_key in existing_keys:
            print(f"   ⏭️  スキップ（既存）: {citation_key}")
            skipped += 1
            continue
        
        # 新規エントリとして追加
        new_entries.append(bibtex)
        if citation_key:
            existing_keys.add(citation_key)
        print(f"   ✅ 追加: {citation_key or 'unknown'}")
        print()
    
    # 結果をファイルに書き込み
    if new_entries:
        with open(bib_file, 'a', encoding='utf-8') as f:
            f.write("\n\n% ===== Auto-generated entries =====\n")
            f.write("\n\n".join(new_entries))
            f.write("\n")
        
        print(f"\n✅ {len(new_entries)}件の新規参考文献を {bib_file} に追加しました")
    else:
        print("\n📝 新規追加なし")
    
    # サマリー
    print("\n" + "="*50)
    print(f"📊 処理結果:")
    print(f"   - 検出したPDF: {len(pdf_files)}個")
    print(f"   - 新規追加: {len(new_entries)}件")
    print(f"   - スキップ（既存）: {skipped}件")
    print(f"   - DOI未検出: {no_doi}件")
    print("="*50 + "\n")
    
    if no_doi > 0:
        print("💡 ヒント: DOI未検出のPDFは手動で追加するか、")
        print("   ファイル名に DOI を含めてください（例: 10.1109_paper.pdf）")

if __name__ == "__main__":
    main()
