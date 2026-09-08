# Codebook: Algorithmic Contestability Cases Database

This document provides detailed definitions for all variables in the dataset and describes the coding methodology.

## Variable Definitions

### case_id
- **Type**: String
- **Format**: `{DOMAIN_PREFIX}-{NUMBER}`
- **Description**: Unique identifier for each case
- **Domain Prefixes**:
  - `EMP` = Employment
  - `HOU` = Housing
  - `HLT` = Healthcare
  - `CJ` = Criminal Justice
  - `GOV` = Government Benefits
  - `CRD` = Credit, Insurance, and Consumer

### case_name
- **Type**: String
- **Description**: Primary identifying name of the case, regulatory action, or system
- **Format**: Typically follows legal citation style (e.g., "Plaintiff v. Defendant") or describes the system/program name for regulatory actions

### year
- **Type**: Integer
- **Range**: 2012-2025
- **Description**: Year of primary legal action, settlement, or resolution. For ongoing cases, year of most recent significant development.

### domain
- **Type**: Categorical
- **Values**:
  - `Employment` - Hiring, workplace management, gig economy
  - `Housing` - Tenant screening, rental pricing, fair housing
  - `Healthcare` - Insurance, clinical decision support, benefits
  - `Criminal Justice` - Risk assessment, policing, surveillance
  - `Government Benefits` - Welfare, fraud detection, eligibility
  - `Credit` - Lending, insurance, consumer protection

### jurisdiction
- **Type**: String
- **Description**: Geographic jurisdiction where legal action occurred
- **Examples**: "US-Federal", "US-CA" (California), "EU", "UK", "Netherlands", "Australia"

### access_level
- **Type**: Categorical
- **Values**:
  - `Full` - Complete algorithmic transparency achieved
  - `Partial` - Limited technical disclosure obtained
  - `None` - No meaningful technical access despite efforts

#### Coding Rules for Access Level

**Full Access** requires at least one of:
- Source code disclosed to parties or court
- Complete model specifications provided
- Training data made available for review
- Algorithm fully documented in regulatory filings

**Partial Access** includes:
- Feature importance or weight disclosure
- Validation or audit data provided
- Limited documentation (e.g., marketing materials, patents)
- Expert access without full disclosure
- FOIA responses with partial technical information

**None** applies when:
- Discovery requests denied or limited
- Trade secret claims upheld
- No technical information obtained despite litigation
- Challenge dismissed before discovery

### outcome
- **Type**: Categorical
- **Values**:
  - `Achieved` - Substantive relief obtained
  - `Denied` - Challenge rejected or dismissed
  - `Ongoing` - Active litigation or investigation

#### Coding Rules for Outcome

**Achieved** requires at least one of:
- Monetary damages or settlement
- Injunctive relief granted
- Policy or system changes implemented
- Algorithm modified or discontinued
- Regulatory enforcement action completed

**Denied** applies when:
- Motion to dismiss granted
- Summary judgment for defendant
- Arbitration enforced without relief
- Administrative challenge rejected
- Appeals exhausted without relief

**Ongoing** applies when:
- Active litigation pending
- Regulatory investigation in progress
- Appeal pending
- Settlement negotiations ongoing

### notes
- **Type**: String
- **Description**: Brief summary of key facts, outcome details, and settlement amounts where applicable
- **Format**: Abbreviated for space; see primary sources for full details

### legal_citation
- **Type**: String (nullable)
- **Description**: Primary legal citation, docket number, or regulatory filing identifier
- **Format**: Standard legal citation format (e.g., "123 F.3d 456 (9th Cir. 2023)")
- **Note**: May be blank for cases without formal legal filings

### docket_number
- **Type**: String (nullable)
- **Description**: Court docket number or regulatory case identifier
- **Format**: Standard format (e.g., "1:22-cv-02565 (E.D.N.Y.)" for federal cases)

### primary_source_url
- **Type**: String (nullable)
- **Description**: URL to authoritative primary source
- **Priority Order**:
  1. Official court/agency records (PACER, FTC.gov, CFPB.gov, etc.)
  2. Government press releases
  3. Official court opinions (CourtListener, Google Scholar)
  4. International official sources (CURIA, BAILII, national DPAs)

### secondary_source_url
- **Type**: String (nullable)
- **Description**: URL to secondary/backup source
- **Acceptable Sources**: Academic papers with DOI, quality journalism (NYT, Reuters, ProPublica, The Markup), legal news (Law360)

### verification_status
- **Type**: Categorical
- **Values**:
  - `Verified` - Primary source URL confirmed accessible and accurate
  - `Needs Review` - Case documented but requires additional source verification
  - `Unable to Verify` - Cannot locate authoritative primary source

### last_verified
- **Type**: Date
- **Format**: YYYY-MM-DD
- **Description**: Date when verification status was last confirmed

## Source Hierarchy

Sources are prioritized in the following order:

1. **Tier 1 - Official Records** (strongest)
   - Federal court filings (PACER)
   - Agency enforcement databases (FTC, CFPB, EEOC, DOJ)
   - State court electronic filing systems
   - International court databases (CURIA, BAILII, CanLII)

2. **Tier 2 - Government Communications**
   - Agency press releases
   - Regulatory announcements
   - Official settlement documents

3. **Tier 3 - Legal Databases**
   - CourtListener (free federal opinions)
   - Google Scholar Case Law
   - Casetext

4. **Tier 4 - Academic Sources**
   - Peer-reviewed papers with DOI
   - Law review articles
   - Working papers from recognized institutions

5. **Tier 5 - Quality Journalism**
   - Major outlets (NYT, WSJ, Reuters, Washington Post)
   - Investigative journalism (ProPublica, The Markup)
   - Trade press (Law360, Healthcare Dive) - secondary only

## Coding Methodology

### Inter-Coder Reliability

[To be completed - describe reliability testing if performed]

### Ambiguous Cases

When coding was ambiguous, the following rules were applied:

1. **Multiple outcomes**: Code based on primary or most significant outcome
2. **Partial settlements**: Code as "Achieved" if substantive relief obtained
3. **Appeals pending**: Code as "Ongoing" unless lower court decision is final
4. **Confidential settlements**: Code based on publicly available information only

### Data Quality

- All cases verified against at least one primary source
- Legal citations verified against court records where available
- Ongoing cases reviewed for status as of [date]

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-27 | Initial release |
| 1.1 | 2025-01-27 | Added verification fields (docket_number, primary_source_url, secondary_source_url, verification_status, last_verified); Added source hierarchy documentation; 97/154 cases verified with primary sources |
