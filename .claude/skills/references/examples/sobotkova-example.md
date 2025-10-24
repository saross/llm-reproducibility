# Extraction Example - Sobotkova et al. 2023 (Methods Section)

This example shows how the Research Assessor workflow extracts RDMAP (Research Designs, Methods, Protocols) from a real paper.

## Source Paper

**Sobotkova, A., Ross, S. A., Ballsun-Stanton, B., Fairbairn, A., Thompson, J., & VanValkenburgh, P. (2023).** Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform. In *Mobilizing the Past for a Digital Future* (pp. 80–105). Ubiquity Press.

## Example Extraction Sequence

### Step 1: Research Design Extraction

**RD001 - Study Design:**
```json
{
  "design_id": "RD001",
  "design_text": "Comparative evaluation of mobile versus traditional paper-based archaeological field recording methods",
  "design_type": "study_design",
  "study_design": {
    "design_type": "comparative",
    "rationale": "Assess effectiveness of mobile data collection platform for archaeological survey",
    "alternatives_considered": ["Traditional paper-based recording"]
  },
  "enables_methods": ["M003", "M008"],
  "reasoning_approach": {"approach": "abductive"},
  "location": {"section": "Introduction", "page": 2, "paragraph": 3}
}
```

### Step 2: Method Extraction

**M008 - Data Collection Method:**
```json
{
  "method_id": "M008",
  "method_text": "Mobile platform (FAIMS Mobile) used for field data collection during archaeological survey",
  "method_type": "data_collection",
  "data_collection_approach": {
    "approach": "survey",
    "domain_specific_type": "pedestrian archaeological survey"
  },
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023", "P024", "P025"],
  "validated_by_evidence": ["E046"],
  "location": {"section": "Methods", "page": 4, "paragraph": 2}
}
```

### Step 3: Protocol Extraction

**P023 - Recording Platform:**
```json
{
  "protocol_id": "P023",
  "protocol_text": "FAIMS Mobile v2.6 configured with custom archaeological survey module for Android devices",
  "protocol_type": "recording",
  "tools": [{
    "tool_name": "FAIMS Mobile",
    "tool_type": "software",
    "version": "2.6",
    "platform": "Android",
    "configuration": "Custom archaeological survey module with ceramic recording, GPS integration, and photo capture"
  }],
  "implements_methods": ["M008"],
  "produces_evidence": ["E045"],
  "location": {"section": "Methods", "page": 5, "paragraph": 1}
}
```

**P024 - GPS Protocol:**
```json
{
  "protocol_id": "P024",
  "protocol_text": "GPS coordinates captured using Garmin GPSMAP 64s in WGS84 decimal degrees with ±3-5m horizontal accuracy at HDOP <2.0",
  "protocol_type": "measurement",
  "tools": [{
    "tool_name": "Garmin GPSMAP 64s",
    "tool_type": "gps_device"
  }],
  "measurement_specification": {
    "domain": "Spatial location",
    "instrument": "Garmin GPSMAP 64s",
    "metric": "WGS84 decimal degrees",
    "precision": "±3-5m horizontal accuracy at HDOP <2.0",
    "quality_control": ["HDOP monitoring", "Satellite count check"]
  },
  "implements_methods": ["M008"],
  "produces_evidence": ["E047"],
  "location": {"section": "Methods", "page": 6, "paragraph": 2}
}
```

### Step 4: Cross-References to Claims and Evidence

**C027 - Methodological Justification:**
```json
{
  "claim_id": "C027",
  "claim_text": "Mobile platform provides significant efficiency gains over traditional paper-based recording",
  "claim_type": "methodological_argument",
  "supports_method": "M008",
  "supported_by_evidence": ["E046", "E052"],
  "location": {"section": "Discussion", "page": 12, "paragraph": 3}
}
```

**E046 - Method Validation Evidence:**
```json
{
  "evidence_id": "E046",
  "evidence_text": "Platform recorded 8,343 features across 22 sites with 54 seconds average time per feature",
  "evidence_type": "quantitative_observation",
  "supports_claims": ["C027"],
  "validates_methods": ["M008"],
  "location": {"section": "Results", "page": 8, "paragraph": 2}
}
```

## The Complete Hierarchy

```
Research Design (WHY)
│
├── RD001: Comparative evaluation
│   │
│   ├── Method (WHAT)
│   │   │
│   │   ├── M008: Mobile data collection
│   │   │   │
│   │   │   ├── Protocol (HOW)
│   │   │   │   ├── P023: FAIMS Mobile v2.6 configuration
│   │   │   │   ├── P024: GPS protocol (Garmin GPSMAP 64s)
│   │   │   │   └── P025: Photo capture protocol
│   │   │   │
│   │   │   ├── Validated by
│   │   │   │   └── E046: 8,343 features recorded
│   │   │   │
│   │   │   └── Justified by
│   │   │       └── C027: Efficiency claim
```

## Pass 1 vs Pass 2 Changes

**Pass 1 (Liberal Extraction):**
- Extracted 15 RDMAP items
- Some over-granular (individual GPS settings as separate protocols)
- Some tier uncertainties marked

**Pass 2 (Rationalization):**
- Consolidated to 12 RDMAP items (20% reduction)
- Merged GPS settings into single protocol (P024)
- Refined tier assignments
- Formalized all cross-references

**Example consolidation:**
```json
// Pass 1 had separate items:
P024a: "GPS coordinate system: WGS84 decimal degrees"
P024b: "GPS accuracy: ±3-5m at HDOP <2.0"
P024c: "GPS quality control: HDOP monitoring"

// Pass 2 consolidated to:
P024: "GPS coordinates captured using Garmin GPSMAP 64s in WGS84 
       decimal degrees with ±3-5m horizontal accuracy at HDOP <2.0"
       
consolidation_metadata: {
  "consolidated_from": ["P1_P024a", "P1_P024b", "P1_P024c"],
  "consolidation_type": "compound_finding",
  "information_preserved": "complete",
  "rationale": "GPS specifications assessed together as measurement protocol"
}
```

## Key Observations

1. **Clear hierarchy:** Design → Methods → Protocols flows logically
2. **Cross-references work:** Claims justify methods, evidence validates them
3. **Assessment-ready:** Sufficient detail to evaluate transparency and replicability
4. **Traceable:** All items link to source paper locations
5. **Complete metadata:** Consolidations fully documented

## Full Extraction

The complete extraction from this paper includes:
- 12 Research Designs
- 35 Methods
- 28 Protocols
- 34 Claims
- 27 Evidence items
- 8 Implicit Arguments

Total: 144 items systematically organized with 200+ cross-references.

## Using This Example

When uncertain about:
- **Tier assignment:** Compare to this hierarchy
- **Granularity:** Match this level of detail
- **Cross-references:** Follow these linking patterns
- **Consolidation:** See how over-granular items were merged
