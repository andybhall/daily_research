# Non-US / non-English × AI — probe log, 2026-08-25 (frontier 7)

## Top find — China CAC generative-AI / algorithm registry
Verified this run from multiple analyst sources: the world's only comprehensive, publicly
accessible registry of generative-AI tools — every public-facing generative-AI service
(text/image/audio/video/multimodal) must register before deployment. Each filing's fields:
**registration number, approval date, tool name, company name, province, functional
description, business model (B2B/B2C)**.
Scale: **3,739 generative algorithmic tools from ~2,353 companies (Apr 2025) →
5,822 entries from 3,787 entities (Nov 2025)**, growing ~250–300/month; 988 gen-AI
services + 598 registrations filed by 30 Jun 2026. Includes DeepSeek, Ernie Bot.
Official portal: beian.cac.gov.cn.

**Could not fully probe:** the portal's list API (beian.cac.gov.cn/api/algorithmpublicity/list)
returns HTTP 200 but `{"errno":440,"errmsg":"检测到未登录状态，请先登录"}` (login required);
www.cac.gov.cn was unreachable from here (HTTP 000). Analysts work from CAC's periodic bulk
Excel announcements. Figures above are from analyst/press pages fetched this run, not a raw pull.

## Runner-up — European public-sector AI registers (beyond the NL register)
Germany's "marketplace of AI opportunities" held **1,305 registered AI projects** at extraction;
France runs four public-algorithm repositories (incl. France Travail); the EU JRC maintains a
Public Sector Tech database. A fragmented non-US algorithmic-government panel. (NL register was
logged 2026-08-13.)

## Runner-up — India AI-in-elections
2024 general election: parties spent ~US$50M on authorized AI-generated campaign content,
~40 campaigns used generative AI; Google's Shakti fact-checking collective (300+ journalists,
50+ newsrooms) found only ~2% of reviewed stories were deepfakes/AI. Fragmented across
fact-check outputs and reports (no single clean deposit).
