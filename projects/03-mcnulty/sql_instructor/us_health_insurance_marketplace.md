# US Health Insurance Marketplace

The Health Insurance Marketplace Public Use Files contain data on health and dental plans offered to individuals and small businesses through the US Health Insurance Marketplace.

## Benefits cost sharing

Note: this table is extremely large (5 million rows) and is slow to import.

```sql
CREATE TABLE benefits_cost_sharing (
    BenefitName            varchar,
    BusinessYear           numeric,
    CoinsInnTier1          varchar,
    CoinsInnTier2          varchar,
    CoinsOutofNet          varchar,
    CopayInnTier1          varchar,
    CopayInnTier2          varchar,
    CopayOutofNet          varchar,
    EHBVarReason           varchar,
    Exclusions             varchar,
    Explanation            varchar,
    ImportDate             varchar,
    IsCovered              varchar,
    IsEHB                  varchar,
    IsExclFromInnMOOP      varchar,
    IsExclFromOonMOOP      varchar,
    IsStateMandate         varchar,
    IsSubjToDedTier1       varchar,
    IsSubjToDedTier2       varchar,
    IssuerId               numeric,
    IssuerId2              numeric,
    LimitQty               numeric,
    LimitUnit              varchar,
    MinimumStay            numeric,
    PlanId                 varchar,
    QuantLimitOnSvc        varchar,
    RowNumber              numeric,
    SourceName             varchar,
    StandardComponentId    varchar,
    StateCode              varchar,
    StateCode2             varchar,
    VersionNum             numeric);

COPY benefits_cost_sharing
FROM '/home/ubuntu/health_insurance/BenefitsCostSharing.csv'
DELIMITER ','
CSV HEADER;
```

## Business rules

```sql
CREATE TABLE business_rules (
    BusinessYear                             numeric,
    StateCode                                varchar,
    IssuerId                                 numeric,
    SourceName                               varchar,
    VersionNum                               numeric,
    ImportDate                               varchar,
    IssuerId2                                numeric,
    TIN                                      varchar,
    ProductId                                varchar,
    StandardComponentId                      varchar,
    EnrolleeContractRateDeterminationRule    varchar,
    TwoParentFamilyMaxDependentsRule         varchar,
    SingleParentFamilyMaxDependentsRule      varchar,
    DependentMaximumAgRule                   varchar,
    ChildrenOnlyContractMaxChildrenRule      varchar,
    DomesticPartnerAsSpouseIndicator         varchar,
    SameSexPartnerAsSpouseIndicator          varchar,
    AgeDeterminationRule                     varchar,
    MinimumTobaccoFreeMonthsRule             varchar,
    CohabitationRule                         varchar,
    RowNumber                                numeric,
    MarketCoverage                           varchar,
    DentalOnlyPlan                           varchar);

COPY business_rules
FROM '/home/ubuntu/health_insurance/BusinessRules.csv'
DELIMITER ','
CSV HEADER;
```

## Crosswalk 2015

A table that facilitates joining across years.

```sql
CREATE TABLE crosswalk_2015 (
    State                        varchar,
    DentalPlan                   varchar,
    PlanID_2014                  varchar,
    IssuerID_2014                numeric,
    MultistatePlan_2014          varchar,
    MetalLevel_2014              varchar,
    ChildAdultOnly_2014          numeric,
    FIPSCode                     numeric,
    ZipCode                      numeric,
    CrosswalkLevel               numeric,
    ReasonForCrosswalk           numeric,
    PlanID_2015                  varchar,
    IssuerID_2015                numeric,
    MultistatePlan_2015          varchar,
    MetalLevel_2015              varchar,
    ChildAdultOnly_2015          varchar,
    AgeOffPlanID_2015            varchar,
    IssuerID_AgeOff2015          numeric,
    MultistatePlan_AgeOff2015    varchar,
    MetalLevel_AgeOff2015        varchar,
    ChildAdultOnly_AgeOff2015    varchar);

COPY crosswalk_2015
FROM '/home/ubuntu/health_insurance/Crosswalk2015.csv'
DELIMITER ','
CSV HEADER;
```

## Crosswalk 2016

A table that facilitates joining across years.

```sql
CREATE TABLE crosswalk_2016 (
    State                        varchar,
    DentalPlan                   varchar,
    PlanID_2015                  varchar,
    IssuerID_2015                numeric,
    MultistatePlan_2015          varchar,
    MetalLevel_2015              varchar,
    ChildAdultOnly_2015          numeric,
    FIPSCode                     numeric,
    ZipCode                      numeric,
    CrosswalkLevel               numeric,
    ReasonForCrosswalk           numeric,
    PlanID_2016                  varchar,
    IssuerID_2016                numeric,
    MultistatePlan_2016          varchar,
    MetalLevel_2016              varchar,
    ChildAdultOnly_2016          varchar,
    AgeOffPlanID_2016            varchar,
    IssuerID_AgeOff2016          numeric,
    MultistatePlan_AgeOff2016    varchar,
    MetalLevel_AgeOff2016        varchar,
    ChildAdultOnly_AgeOff2016    varchar);

COPY crosswalk_2016
FROM '/home/ubuntu/health_insurance/Crosswalk2016.csv'
DELIMITER ','
CSV HEADER;
```

## Network

```sql
CREATE TABLE network (
    BusinessYear      numeric,
    StateCode         varchar,
    IssuerId          numeric,
    SourceName        varchar,
    VersionNum        numeric,
    ImportDate        varchar,
    IssuerId2         numeric,
    StateCode2        varchar,
    NetworkName       varchar,
    NetworkId         varchar,
    NetworkURL        varchar,
    RowNumber         numeric,
    MarketCoverage    varchar,
    DentalOnlyPlan    varchar);

COPY network
FROM '/home/ubuntu/health_insurance/Network.csv'
DELIMITER ','
CSV HEADER;
```

## Plan attributes

```sql
CREATE TABLE plan_attributes (
    AVCalculatorOutputNumber                                        varchar,
    BeginPrimaryCareCostSharingAfterNumberOfVisits                  numeric,
    BeginPrimaryCareDeductibleCoinsuranceAfterNumberOfCopays        numeric,
    BenefitPackageId                                                numeric,
    BusinessYear                                                    numeric,
    CSRVariationType                                                varchar,
    ChildOnlyOffering                                               varchar,
    ChildOnlyPlanId                                                 varchar,
    CompositeRatingOffered                                          varchar,
    DEHBCombInnOonFamilyMOOP                                        varchar,
    DEHBCombInnOonFamilyPerGroupMOOP                                varchar,
    DEHBCombInnOonFamilyPerPersonMOOP                               varchar,
    DEHBCombInnOonIndividualMOOP                                    varchar,
    DEHBDedCombInnOonFamily                                         varchar,
    DEHBDedCombInnOonFamilyPerGroup                                 varchar,
    DEHBDedCombInnOonFamilyPerPerson                                varchar,
    DEHBDedCombInnOonIndividual                                     varchar,
    DEHBDedInnTier1Coinsurance                                      varchar,
    DEHBDedInnTier1Family                                           varchar,
    DEHBDedInnTier1FamilyPerGroup                                   varchar,
    DEHBDedInnTier1FamilyPerPerson                                  varchar,
    DEHBDedInnTier1Individual                                       varchar,
    DEHBDedInnTier2Coinsurance                                      varchar,
    DEHBDedInnTier2Family                                           varchar,
    DEHBDedInnTier2FamilyPerGroup                                   varchar,
    DEHBDedInnTier2FamilyPerPerson                                  varchar,
    DEHBDedInnTier2Individual                                       varchar,
    DEHBDedOutOfNetFamily                                           varchar,
    DEHBDedOutOfNetFamilyPerGroup                                   varchar,
    DEHBDedOutOfNetFamilyPerPerson                                  varchar,
    DEHBDedOutOfNetIndividual                                       varchar,
    DEHBInnTier1FamilyMOOP                                          varchar,
    DEHBInnTier1FamilyPerGroupMOOP                                  varchar,
    DEHBInnTier1FamilyPerPersonMOOP                                 varchar,
    DEHBInnTier1IndividualMOOP                                      varchar,
    DEHBInnTier2FamilyMOOP                                          numeric,
    DEHBInnTier2FamilyPerGroupMOOP                                  numeric,
    DEHBInnTier2FamilyPerPersonMOOP                                 numeric,
    DEHBInnTier2IndividualMOOP                                      numeric,
    DEHBOutOfNetFamilyMOOP                                          varchar,
    DEHBOutOfNetFamilyPerGroupMOOP                                  varchar,
    DEHBOutOfNetFamilyPerPersonMOOP                                 varchar,
    DEHBOutOfNetIndividualMOOP                                      varchar,
    DentalOnlyPlan                                                  varchar,
    DiseaseManagementProgramsOffered                                varchar,
    EHBPediatricDentalApportionmentQuantity                         varchar,
    EHBPercentPremiumS4                                             numeric,
    EHBPercentTotalPremium                                          numeric,
    FirstTierUtilization                                            varchar,
    FormularyId                                                     varchar,
    FormularyURL                                                    varchar,
    HIOSProductId                                                   varchar,
    HPID                                                            numeric,
    HSAOrHRAEmployerContribution                                    varchar,
    HSAOrHRAEmployerContributionAmount                              varchar,
    ImportDate                                                      varchar,
    IndianPlanVariationEstimatedAdvancedPaymentAmountPerEnrollee    varchar,
    InpatientCopaymentMaximumDays                                   numeric,
    IsGuaranteedRate                                                varchar,
    IsHSAEligible                                                   varchar,
    IsNewPlan                                                       varchar,
    IsNoticeRequiredForPregnancy                                    varchar,
    IsReferralRequiredForSpecialist                                 varchar,
    IssuerActuarialValue                                            varchar,
    IssuerId                                                        numeric,
    IssuerId2                                                       numeric,
    MEHBCombInnOonFamilyMOOP                                        varchar,
    MEHBCombInnOonFamilyPerGroupMOOP                                varchar,
    MEHBCombInnOonFamilyPerPersonMOOP                               varchar,
    MEHBCombInnOonIndividualMOOP                                    varchar,
    MEHBDedCombInnOonFamily                                         varchar,
    MEHBDedCombInnOonFamilyPerGroup                                 varchar,
    MEHBDedCombInnOonFamilyPerPerson                                varchar,
    MEHBDedCombInnOonIndividual                                     varchar,
    MEHBDedInnTier1Coinsurance                                      varchar,
    MEHBDedInnTier1Family                                           varchar,
    MEHBDedInnTier1FamilyPerGroup                                   varchar,
    MEHBDedInnTier1FamilyPerPerson                                  varchar,
    MEHBDedInnTier1Individual                                       varchar,
    MEHBDedInnTier2Coinsurance                                      varchar,
    MEHBDedInnTier2Family                                           varchar,
    MEHBDedInnTier2FamilyPerGroup                                   varchar,
    MEHBDedInnTier2FamilyPerPerson                                  varchar,
    MEHBDedInnTier2Individual                                       varchar,
    MEHBDedOutOfNetFamily                                           varchar,
    MEHBDedOutOfNetFamilyPerGroup                                   varchar,
    MEHBDedOutOfNetFamilyPerPerson                                  varchar,
    MEHBDedOutOfNetIndividual                                       varchar,
    MEHBInnTier1FamilyMOOP                                          varchar,
    MEHBInnTier1FamilyPerGroupMOOP                                  varchar,
    MEHBInnTier1FamilyPerPersonMOOP                                 varchar,
    MEHBInnTier1IndividualMOOP                                      varchar,
    MEHBInnTier2FamilyMOOP                                          varchar,
    MEHBInnTier2FamilyPerGroupMOOP                                  varchar,
    MEHBInnTier2FamilyPerPersonMOOP                                 varchar,
    MEHBInnTier2IndividualMOOP                                      varchar,
    MEHBOutOfNetFamilyMOOP                                          varchar,
    MEHBOutOfNetFamilyPerGroupMOOP                                  varchar,
    MEHBOutOfNetFamilyPerPersonMOOP                                 varchar,
    MEHBOutOfNetIndividualMOOP                                      varchar,
    MarketCoverage                                                  varchar,
    MedicalDrugDeductiblesIntegrated                                varchar,
    MedicalDrugMaximumOutofPocketIntegrated                         varchar,
    MetalLevel                                                      varchar,
    MultipleInNetworkTiers                                          varchar,
    NationalNetwork                                                 varchar,
    NetworkId                                                       varchar,
    OutOfCountryCoverage                                            varchar,
    OutOfCountryCoverageDescription                                 varchar,
    OutOfServiceAreaCoverage                                        varchar,
    OutOfServiceAreaCoverageDescription                             varchar,
    PlanBrochure                                                    varchar,
    PlanEffictiveDate                                               varchar,
    PlanExpirationDate                                              varchar,
    PlanId                                                          varchar,
    PlanLevelExclusions                                             varchar,
    PlanMarketingName                                               varchar,
    PlanType                                                        varchar,
    QHPNonQHPTypeId                                                 varchar,
    RowNumber                                                       numeric,
    SBCHavingDiabetesCoinsurance                                    varchar,
    SBCHavingDiabetesCopayment                                      varchar,
    SBCHavingDiabetesDeductible                                     varchar,
    SBCHavingDiabetesLimit                                          varchar,
    SBCHavingaBabyCoinsurance                                       varchar,
    SBCHavingaBabyCopayment                                         varchar,
    SBCHavingaBabyDeductible                                        varchar,
    SBCHavingaBabyLimit                                             varchar,
    SecondTierUtilization                                           varchar,
    ServiceAreaId                                                   varchar,
    SourceName                                                      varchar,
    SpecialistRequiringReferral                                     varchar,
    SpecialtyDrugMaximumCoinsurance                                 varchar,
    StandardComponentId                                             varchar,
    StateCode                                                       varchar,
    StateCode2                                                      varchar,
    TEHBCombInnOonFamilyMOOP                                        varchar,
    TEHBCombInnOonFamilyPerGroupMOOP                                varchar,
    TEHBCombInnOonFamilyPerPersonMOOP                               varchar,
    TEHBCombInnOonIndividualMOOP                                    varchar,
    TEHBDedCombInnOonFamily                                         varchar,
    TEHBDedCombInnOonFamilyPerGroup                                 varchar,
    TEHBDedCombInnOonFamilyPerPerson                                varchar,
    TEHBDedCombInnOonIndividual                                     varchar,
    TEHBDedInnTier1Coinsurance                                      varchar,
    TEHBDedInnTier1Family                                           varchar,
    TEHBDedInnTier1FamilyPerGroup                                   varchar,
    TEHBDedInnTier1FamilyPerPerson                                  varchar,
    TEHBDedInnTier1Individual                                       varchar,
    TEHBDedInnTier2Coinsurance                                      varchar,
    TEHBDedInnTier2Family                                           varchar,
    TEHBDedInnTier2FamilyPerGroup                                   varchar,
    TEHBDedInnTier2FamilyPerPerson                                  varchar,
    TEHBDedInnTier2Individual                                       varchar,
    TEHBDedOutOfNetFamily                                           varchar,
    TEHBDedOutOfNetFamilyPerGroup                                   varchar,
    TEHBDedOutOfNetFamilyPerPerson                                  varchar,
    TEHBDedOutOfNetIndividual                                       varchar,
    TEHBInnTier1FamilyMOOP                                          varchar,
    TEHBInnTier1FamilyPerGroupMOOP                                  varchar,
    TEHBInnTier1FamilyPerPersonMOOP                                 varchar,
    TEHBInnTier1IndividualMOOP                                      varchar,
    TEHBInnTier2FamilyMOOP                                          varchar,
    TEHBInnTier2FamilyPerGroupMOOP                                  varchar,
    TEHBInnTier2FamilyPerPersonMOOP                                 varchar,
    TEHBInnTier2IndividualMOOP                                      varchar,
    TEHBOutOfNetFamilyMOOP                                          varchar,
    TEHBOutOfNetFamilyPerGroupMOOP                                  varchar,
    TEHBOutOfNetFamilyPerPersonMOOP                                 varchar,
    TEHBOutOfNetIndividualMOOP                                      varchar,
    TIN                                                             varchar,
    URLForEnrollmentPayment                                         varchar,
    URLForSummaryofBenefitsCoverage                                 varchar,
    UniquePlanDesign                                                varchar,
    VersionNum                                                      numeric,
    WellnessProgramOffered                                          varchar);

COPY plan_attributes
FROM '/home/ubuntu/health_insurance/PlanAttributes.csv'
DELIMITER ','
CSV HEADER;
```

## Rate

Note: this table is extremely large (12.7 million rows) and is slow to import.

```sql
CREATE TABLE rate (
    BusinessYear                                 numeric,
    StateCode                                    varchar,
    IssuerId                                     numeric,
    SourceName                                   varchar,
    VersionNum                                   numeric,
    ImportDate                                   varchar,
    IssuerId2                                    numeric,
    FederalTIN                                   varchar,
    RateEffectiveDate                            varchar,
    RateExpirationDate                           varchar,
    PlanId                                       varchar,
    RatingAreaId                                 varchar,
    Tobacco                                      varchar,
    Age                                          varchar,
    IndividualRate                               numeric,
    IndividualTobaccoRate                        numeric,
    Couple                                       numeric,
    PrimarySubscriberAndOneDependent             numeric,
    PrimarySubscriberAndTwoDependents            numeric,
    PrimarySubscriberAndThreeOrMoreDependents    numeric,
    CoupleAndOneDependent                        numeric,
    CoupleAndTwoDependents                       numeric,
    CoupleAndThreeOrMoreDependents               numeric,
    RowNumber                                    numeric);

COPY rate
FROM '/home/ubuntu/health_insurance/Rate.csv'
DELIMITER ','
CSV HEADER;
```

## Service area

```sql
CREATE TABLE service_area (
    BusinessYear                  numeric,
    StateCode                     varchar,
    IssuerId                      numeric,
    SourceName                    varchar,
    VersionNum                    numeric,
    ImportDate                    varchar,
    IssuerId2                     numeric,
    StateCode2                    varchar,
    ServiceAreaId                 varchar,
    ServiceAreaName               varchar,
    CoverEntireState              varchar,
    County                        numeric,
    PartialCounty                 varchar,
    ZipCodes                      varchar,
    PartialCountyJustification    varchar,
    RowNumber                     numeric,
    MarketCoverage                varchar,
    DentalOnlyPlan                varchar);

COPY service_area
FROM '/home/ubuntu/health_insurance/ServiceArea.csv'
DELIMITER ','
CSV HEADER;
```