# Probe — Brazilian electoral deepfake jurisprudence corpus (Zenodo 22013413)

**Source:** Zenodo record 22013413, "Dataset: deepfakes e jurisprudência eleitoral
brasileira (2023–2026)" (CC-BY-4.0, published 2026-08-19, **47 downloads / 131 views**).
A PIBIC (undergraduate research) project. Pulled `deepfakes_levantamento_v2.csv` +
variable dictionary this run.

## Computed this run (n = 129 documents, 11 coded fields)
Fields: id, jurisdicao, secao, referencia_completa, autor_orgao, tipo_documento,
tipo_grupo, temas_centrais, resumo_analitico, localizacao, url.

- **By document type** (`br_deepfake_by_type.csv`): institutional documents/reports
  **56**, **judicial precedents 47**, resolutions/ordinances 16, legislation 10.
- **Authoring bodies:** the Brazilian electoral core is TSE (5) + regional electoral
  courts (TRE-PE 5, TRE-SP 5, TRE-GO 4, TRE-MA 4, TRE-MG 4, …); the corpus also folds
  in international-instrument context (UN General Assembly 17, CIDH 6, UNICEF 6).
- **Year mentions** (rough, from references/summaries): 2024 **59**, 2025 26, 2026 21
  — tracking the municipal-2024 → general-2026 election cycles.
- **Central themes:** Deepfakes 111, Liberdade de Expressão (free speech) 22,
  Inteligência Artificial 13, Propaganda Eleitoral 12, WhatsApp 9, Desinformação
  Eleitoral 9, Sátira Política 6 (satire — the recurring defense).

## Context (reporting, cited in memo — NOT from this dataset)
- Of **591 deepfake-related decisions in the 2024 municipal elections, ~20%
  recognized manipulation while 62% treated the content as satire/humor**
  (Rio Times). TSE Resolution 23.755 (Mar 2026) bans electoral deepfakes and
  mandates AI-content labeling.

## Why it's a distinct, on-frontier object
A **non-US, non-English (Portuguese)** judicial + normative view of AI in elections —
how Brazilian electoral courts and bodies actually adjudicate deepfakes — distinct
from the US-centric PDID (08-18) and the Canadian-election measurement (08-28).
Panel-able by body × document-type × theme × year.

## Files
- `deepfakes_levantamento_v2.csv` — the 129-document coded corpus.
- `dicionario-de-variaveis.md` — variable dictionary.
- `br_deepfake_by_type.csv` — documents by type (chart source).
