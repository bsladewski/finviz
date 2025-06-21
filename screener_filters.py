from enum import Enum

class Filters(object):
    """
    Provides filter parameters for interacting with the FinViz Screening site.
    """

    def __init__(self, manual_filters: list[str] | None=None):
        self.filters = {}
        self.manual_filters = manual_filters or []

    class Exchange(str, Enum):
        """
        Stock Exchange at which a stock is listed.
        """
        AMEX='exch_amex'
        CBOE='exch_cboe'
        NASDAQ='exch_nasd'
        NYSE='exch_nyse'

    def filter_exchange(self, exchange: Exchange):
        self.filters['Exchange'] = exchange

    class Index(str, Enum):
        """
        A major index membership of a stock.
        """
        S_AND_P_FIVE_HUNDRED='idx_sp500'
        NASDAQ_ONE_HUNDRED='idx_ndx'
        DJIA='idx_dji'
        RUSSELL_TWO_THOUSAND='idx_rut'

    def filter_index(self, index: Index):
        self.filters['Index'] = index

    class Sector(str, Enum):
        """
        The sector which a stock belongs to.
        """
        BASIC_MATERIALS='sec_basicmaterials'
        COMMUNICATION_SERVICES='sec_communicationservices'
        CONSUMER_CYCLICAL='sec_consumercyclical'
        CONSUMER_DEFENSIVE='sec_consumerdefensive'
        ENERGY='sec_energy'
        FINANCIAL='sec_financial'
        HEALTHCARE='sec_healthcare'
        INDUSTRIALS='sec_industrials'
        REAL_ESTATE='sec_realestate'
        TECHNOLOGY='sec_technology'
        UTILITIES='sec_utilities'

    def filter_sector(self, sector: Sector):
        self.filters['Sector'] = sector

    class Industry(str, Enum):
        """
        The industry which a stock belongs to.
        """
        STOCKS_ONLY_EX_FUNDS='ind_stocksonly'
        EXCHANGE_TRADED_FUND='ind_exchangetradedfund'
        ADVERTISING_AGENCIES='ind_advertisingagencies'
        AEROSPACE_AND_DEFENSE='ind_aerospacedefense'
        AGRICULTURAL_INPUTS='ind_agriculturalinputs'
        AIRLINES='ind_airlines'
        AIRPORTS_AND_AIR_SERVICES='ind_airportsairservices'
        ALUMINUM='ind_aluminum'
        APPAREL_MANUFACTURING='ind_apparelmanufacturing'
        APPAREL_RETAIL='ind_apparelretail'
        ASSET_MANAGEMENT='ind_assetmanagement'
        AUTO_MANUFACTURERS='ind_automanufacturers'
        AUTO_PARTS='ind_autoparts'
        AUTO_AND_TRUCK_DEALERSHIPS='ind_autotruckdealerships'
        BANKS_DIVERSIFIED='ind_banksdiversified'
        BANKS_REGIONAL='ind_banksregional'
        BEVERAGES_BREWERS='ind_beveragesbrewers'
        BEVERAGES_NON_ALCOHOLIC='ind_beveragesnonalcoholic'
        BEVERAGES_WINERIES_AND_DISTILLERIES='ind_beverageswineriesdistilleries'
        BIOTECHNOLOGY='ind_biotechnology'
        BROADCASTING='ind_broadcasting'
        BUILDING_MATERIALS='ind_buildingmaterials'
        BUILDING_PRODUCTS_AND_EQUIPMENT='ind_buildingproductsequipment'
        BUSINESS_EQUIPMENT_AND_SUPPLIES='ind_businessequipmentsupplies'
        CAPITAL_MARKETS='ind_capitalmarkets'
        CHEMICALS='ind_chemicals'
        CLOSED_END_FUND_DEBT='ind_closedendfunddebt'
        CLOSED_END_FUND_EQUITY='ind_closedendfundequity'
        CLOSED_END_FUND_FOREIGN='ind_closedendfundforeign'
        COKING_COAL='ind_cokingcoal'
        COMMUNICATION_EQUIPMENT='ind_communicationequipment'
        COMPUTER_HARDWARE='ind_computerhardware'
        CONFECTIONERS='ind_confectioners'
        CONGLOMERATES='ind_conglomerates'
        CONSULTING_SERVICES='ind_consultingservices'
        CONSUMER_ELECTRONICS='ind_consumerelectronics'
        COPPER='ind_copper'
        CREDIT_SERVICES='ind_creditservices'
        DEPARTMENT_STORES='ind_departmentstores'
        DIAGNOSTICS_AND_RESEARCH='ind_diagnosticsresearch'
        DISCOUNT_STORES='ind_discountstores'
        DRUG_MANUFACTURERS_GENERAL='ind_drugmanufacturersgeneral'
        DRUG_MANUFACTURERS_SPECIALTY_AND_GENERIC='ind_drugmanufacturersspecialtygeneric'
        EDUCATION_AND_TRAINING_SERVICES='ind_educationtrainingservices'
        ELECTRICAL_EQUIPMENT_AND_PARTS='ind_electricalequipmentparts'
        ELECTRONIC_COMPONENTS='ind_electroniccomponents'
        ELECTRONIC_GAMING_AND_MULTIMEDIA='ind_electronicgamingmultimedia'
        ELECTRONICS_AND_COMPUTER_DISTRIBUTION='ind_electronicscomputerdistribution'
        ENGINEERING_AND_CONSTRUCTION='ind_engineeringconstruction'
        ENTERTAINMENT='ind_entertainment'
        FARM_AND_HEAVY_CONSTRUCTION_MACHINERY='ind_farmheavyconstructionmachinery'
        FARM_PRODUCTS='ind_farmproducts'
        FINANCIAL_CONGLOMERATES='ind_financialconglomerates'
        FINANCIAL_DATA_AND_STOCK_EXCHANGES='ind_financialdatastockexchanges'
        FOOD_DISTRIBUTION='ind_fooddistribution'
        FOOTWEAR_AND_ACCESSORIES='ind_footwearaccessories'
        FURNISHINGS_FIXTURES_AND_APPLIANCES='ind_furnishingsfixturesappliances'
        GAMBLING='ind_gambling'
        GOLD='ind_gold'
        GROCERY_STORES='ind_grocerystores'
        HEALTHCARE_PLANS='ind_healthcareplans'
        HEALTH_INFORMATION_SERVICES='ind_healthinformationservices'
        HOME_IMPROVEMENT_RETAIL='ind_homeimprovementretail'
        HOUSEHOLD_AND_PERSONAL_PRODUCTS='ind_householdpersonalproducts'
        INDUSTRIAL_DISTRIBUTION='ind_industrialdistribution'
        INFORMATION_TECHNOLOGY_SERVICES='ind_informationtechnologyservices'
        INFRASTRUCTURE_OPERATIONS='ind_infrastructureoperations'
        INSURANCE_BROKERS='ind_insurancebrokers'
        INSURANCE_DIVERSIFIED='ind_insurancediversified'
        INSURANCE_LIFE='ind_insurancelife'
        INSURANCE_PROPERTY_AND_CASUALTY='ind_insurancepropertycasualty'
        INSURANCE_REINSURANCE='ind_insurancereinsurance'
        INSURANCE_SPECIALTY='ind_insurancespecialty'
        INTEGRATED_FREIGHT_AND_LOGISTICS='ind_integratedfreightlogistics'
        INTERNET_CONTENT_AND_INFORMATION='ind_internetcontentinformation'
        INTERNET_RETAIL='ind_internetretail'
        LEISURE='ind_leisure'
        LODGING='ind_lodging'
        LUMBER_AND_WOOD_PRODUCTION='ind_lumberwoodproduction'
        LUXURY_GOODS='ind_luxurygoods'
        MARINE_SHIPPING='ind_marineshipping'
        MEDICAL_CARE_FACILITIES='ind_medicalcarefacilities'
        MEDICAL_DEVICES='ind_medicaldevices'
        MEDICAL_DISTRIBUTION='ind_medicaldistribution'
        MEDICAL_INSTRUMENTS_AND_SUPPLIES='ind_medicalinstrumentssupplies'
        METAL_FABRICATION='ind_metalfabrication'
        MORTGAGE_FINANCE='ind_mortgagefinance'
        OIL_AND_GAS_DRILLING='ind_oilgasdrilling'
        OIL_AND_GAS_E_AND_P='ind_oilgasep'
        OIL_AND_GAS_EQUIPMENT_AND_SERVICES='ind_oilgasequipmentservices'
        OIL_AND_GAS_INTEGRATED='ind_oilgasintegrated'
        OIL_AND_GAS_MIDSTREAM='ind_oilgasmidstream'
        OIL_AND_GAS_REFINING_AND_MARKETING='ind_oilgasrefiningmarketing'
        OTHER_INDUSTRIAL_METALS_AND_MINING='ind_otherindustrialmetalsmining'
        OTHER_PRECIOUS_METALS_AND_MINING='ind_otherpreciousmetalsmining'
        PACKAGED_FOODS='ind_packagedfoods'
        PACKAGING_AND_CONTAINERS='ind_packagingcontainers'
        PAPER_AND_PAPER_PRODUCTS='ind_paperpaperproducts'
        PERSONAL_SERVICES='ind_personalservices'
        PHARMACEUTICAL_RETAILERS='ind_pharmaceuticalretailers'
        POLLUTION_AND_TREATMENT_CONTROLS='ind_pollutiontreatmentcontrols'
        PUBLISHING='ind_publishing'
        RAILROADS='ind_railroads'
        REAL_ESTATE_DEVELOPMENT='ind_realestatedevelopment'
        REAL_ESTATE_DIVERSIFIED='ind_realestatediversified'
        REAL_ESTATE_SERVICES='ind_realestateservices'
        RECREATIONAL_VEHICLES='ind_recreationalvehicles'
        REIT_DIVERSIFIED='ind_reitdiversified'
        REIT_HEALTHCARE_FACILITIES='ind_reithealthcarefacilities'
        REIT_HOTEL_AND_MOTEL='ind_reithotelmotel'
        REIT_INDUSTRIAL='ind_reitindustrial'
        REIT_MORTGAGE='ind_reitmortgage'
        REIT_OFFICE='ind_reitoffice'
        REIT_RESIDENTIAL='ind_reitresidential'
        REIT_RETAIL='ind_reitretail'
        REIT_SPECIALTY='ind_reitspecialty'
        RENTAL_AND_LEASING_SERVICES='ind_rentalleasingservices'
        RESIDENTIAL_CONSTRUCTION='ind_residentialconstruction'
        RESORTS_AND_CASINOS='ind_resortscasinos'
        RESTAURANTS='ind_restaurants'
        SCIENTIFIC_AND_TECHNICAL_INSTRUMENTS='ind_scientifictechnicalinstruments'
        SECURITY_AND_PROTECTION_SERVICES='ind_securityprotectionservices'
        SEMICONDUCTOR_EQUIPMENT_AND_MATERIALS='ind_semiconductorequipmentmaterials'
        SEMICONDUCTORS='ind_semiconductors'
        SHELL_COMPANIES='ind_shellcompanies'
        SILVER='ind_silver'
        SOFTWARE_APPLICATION='ind_softwareapplication'
        SOFTWARE_INFRASTRUCTURE='ind_softwareinfrastructure'
        SOLAR='ind_solar'
        SPECIALTY_BUSINESS_SERVICES='ind_specialtybusinessservices'
        SPECIALTY_CHEMICALS='ind_specialtychemicals'
        SPECIALTY_INDUSTRIAL_MACHINERY='ind_specialtyindustrialmachinery'
        SPECIALTY_RETAIL='ind_specialtyretail'
        STAFFING_AND_EMPLOYMENT_SERVICES='ind_staffingemploymentservices'
        STEEL='ind_steel'
        TELECOM_SERVICES='ind_telecomservices'
        TEXTILE_MANUFACTURING='ind_textilemanufacturing'
        THERMAL_COAL='ind_thermalcoal'
        TOBACCO='ind_tobacco'
        TOOLS_AND_ACCESSORIES='ind_toolsaccessories'
        TRAVEL_SERVICES='ind_travelservices'
        TRUCKING='ind_trucking'
        URANIUM='ind_uranium'
        UTILITIES_DIVERSIFIED='ind_utilitiesdiversified'
        UTILITIES_INDEPENDENT_POWER_PRODUCERS='ind_utilitiesindependentpowerproducers'
        UTILITIES_REGULATED_ELECTRIC='ind_utilitiesregulatedelectric'
        UTILITIES_REGULATED_GAS='ind_utilitiesregulatedgas'
        UTILITIES_REGULATED_WATER='ind_utilitiesregulatedwater'
        UTILITIES_RENEWABLE='ind_utilitiesrenewable'
        WASTE_MANAGEMENT='ind_wastemanagement'

    def filter_industry(self, industry: Industry):
        self.filters['Industry'] = industry

    class Country(str, Enum):
        """
        The country where company of selected stock is based.
        """
        USA='geo_usa'
        FOREIGN_EX_USA='geo_notusa'
        ASIA='geo_asia'
        EUROPE='geo_europe'
        LATIN_AMERICA='geo_latinamerica'
        BRIC='geo_bric'
        ARGENTINA='geo_argentina'
        AUSTRALIA='geo_australia'
        BAHAMAS='geo_bahamas'
        BELGIUM='geo_belgium'
        BENELUX='geo_benelux'
        BERMUDA='geo_bermuda'
        BRAZIL='geo_brazil'
        CANADA='geo_canada'
        CAYMAN_ISLANDS='geo_caymanislands'
        CHILE='geo_chile'
        CHINA='geo_china'
        CHINA_AND_HONG_KONG='geo_chinahongkong'
        COLOMBIA='geo_colombia'
        CYPRUS='geo_cyprus'
        DENMARK='geo_denmark'
        FINLAND='geo_finland'
        FRANCE='geo_france'
        GERMANY='geo_germany'
        GREECE='geo_greece'
        HONG_KONG='geo_hongkong'
        HUNGARY='geo_hungary'
        ICELAND='geo_iceland'
        INDIA='geo_india'
        INDONESIA='geo_indonesia'
        IRELAND='geo_ireland'
        ISRAEL='geo_israel'
        ITALY='geo_italy'
        JAPAN='geo_japan'
        JORDAN='geo_jordan'
        KAZAKHSTAN='geo_kazakhstan'
        LUXEMBOURG='geo_luxembourg'
        MALAYSIA='geo_malaysia'
        MALTA='geo_malta'
        MEXICO='geo_mexico'
        MONACO='geo_monaco'
        NETHERLANDS='geo_netherlands'
        NEW_ZEALAND='geo_newzealand'
        NORWAY='geo_norway'
        PANAMA='geo_panama'
        PERU='geo_peru'
        PHILIPPINES='geo_philippines'
        PORTUGAL='geo_portugal'
        RUSSIA='geo_russia'
        SINGAPORE='geo_singapore'
        SOUTH_AFRICA='geo_southafrica'
        SOUTH_KOREA='geo_southkorea'
        SPAIN='geo_spain'
        SWEDEN='geo_sweden'
        SWITZERLAND='geo_switzerland'
        TAIWAN='geo_taiwan'
        THAILAND='geo_thailand'
        TURKEY='geo_turkey'
        UNITED_ARAB_EMIRATES='geo_unitedarabemirates'
        UNITED_KINGDOM='geo_unitedkingdom'
        URUGUAY='geo_uruguay'
        VIETNAM='geo_vietnam'

    def filter_country(self, country: Country):
        self.filters['Country'] = country

    class MarketCap(str, Enum):
        """
        Equals The total dollar market value of all of a company's outstanding shares.
        """
        MEGA_DOLLAR_TWO_HUNDRED_BLN_AND_MORE='cap_mega'
        LARGE_DOLLAR_TEN_BLN_TO_DOLLAR_TWO_HUNDRED_BLN='cap_large'
        MID_DOLLAR_TWO_BLN_TO_DOLLAR_TEN_BLN='cap_mid'
        SMALL_DOLLAR_THREE_HUNDRED_MLN_TO_DOLLAR_TWO_BLN='cap_small'
        MICRO_DOLLAR_FIFTY_MLN_TO_DOLLAR_THREE_HUNDRED_MLN='cap_micro'
        NANO_UNDER_DOLLAR_FIFTY_MLN='cap_nano'
        PLUS_LARGE_OVER_DOLLAR_TEN_BLN='cap_largeover'
        PLUS_MID_OVER_DOLLAR_TWO_BLN='cap_midover'
        PLUS_SMALL_OVER_DOLLAR_THREE_HUNDRED_MLN='cap_smallover'
        PLUS_MICRO_OVER_DOLLAR_FIFTY_MLN='cap_microover'
        LARGE_UNDER_DOLLAR_TWO_HUNDRED_BLN='cap_largeunder'
        MID_UNDER_DOLLAR_TEN_BLN='cap_midunder'
        SMALL_UNDER_DOLLAR_TWO_BLN='cap_smallunder'
        MICRO_UNDER_DOLLAR_THREE_HUNDRED_MLN='cap_microunder'

    def filter_market_cap(self, market_cap: MarketCap):
        self.filters['MarketCap'] = market_cap

    class PE(str, Enum):
        """
        A valuation ratio of a company's current share price compared to its per-share earnings (ttm).
        """
        LOW_LESSTHAN_FIFTEEN='fa_pe_low'
        PROFITABLE_GREATERTHAN_ZERO='fa_pe_profitable'
        HIGH_GREATERTHAN_FIFTY='fa_pe_high'
        UNDER_FIVE='fa_pe_u5'
        UNDER_TEN='fa_pe_u10'
        UNDER_FIFTEEN='fa_pe_u15'
        UNDER_TWENTY='fa_pe_u20'
        UNDER_TWENTY_FIVE='fa_pe_u25'
        UNDER_THIRTY='fa_pe_u30'
        UNDER_THIRTY_FIVE='fa_pe_u35'
        UNDER_FORTY='fa_pe_u40'
        UNDER_FORTY_FIVE='fa_pe_u45'
        UNDER_FIFTY='fa_pe_u50'
        OVER_FIVE='fa_pe_o5'
        OVER_TEN='fa_pe_o10'
        OVER_FIFTEEN='fa_pe_o15'
        OVER_TWENTY='fa_pe_o20'
        OVER_TWENTY_FIVE='fa_pe_o25'
        OVER_THIRTY='fa_pe_o30'
        OVER_THIRTY_FIVE='fa_pe_o35'
        OVER_FORTY='fa_pe_o40'
        OVER_FORTY_FIVE='fa_pe_o45'
        OVER_FIFTY='fa_pe_o50'

    def filter_p_e(self, p_e: PE):
        self.filters['PE'] = p_e

    class ForwardPE(str, Enum):
        """
        A measure of the price-to-earnings ratio using forecasted earnings for the P/E calculation. Value for next fiscal year.
        """
        LOW_LESSTHAN_FIFTEEN='fa_fpe_low'
        PROFITABLE_GREATERTHAN_ZERO='fa_fpe_profitable'
        HIGH_GREATERTHAN_FIFTY='fa_fpe_high'
        UNDER_FIVE='fa_fpe_u5'
        UNDER_TEN='fa_fpe_u10'
        UNDER_FIFTEEN='fa_fpe_u15'
        UNDER_TWENTY='fa_fpe_u20'
        UNDER_TWENTY_FIVE='fa_fpe_u25'
        UNDER_THIRTY='fa_fpe_u30'
        UNDER_THIRTY_FIVE='fa_fpe_u35'
        UNDER_FORTY='fa_fpe_u40'
        UNDER_FORTY_FIVE='fa_fpe_u45'
        UNDER_FIFTY='fa_fpe_u50'
        OVER_FIVE='fa_fpe_o5'
        OVER_TEN='fa_fpe_o10'
        OVER_FIFTEEN='fa_fpe_o15'
        OVER_TWENTY='fa_fpe_o20'
        OVER_TWENTY_FIVE='fa_fpe_o25'
        OVER_THIRTY='fa_fpe_o30'
        OVER_THIRTY_FIVE='fa_fpe_o35'
        OVER_FORTY='fa_fpe_o40'
        OVER_FORTY_FIVE='fa_fpe_o45'
        OVER_FIFTY='fa_fpe_o50'

    def filter_forward_p_e(self, forward_p_e: ForwardPE):
        self.filters['ForwardPE'] = forward_p_e

    class Peg(str, Enum):
        """
        A ratio used to determine a stock's value while taking into account earnings growth.
        """
        LOW_LESSTHAN_ONE='fa_peg_low'
        HIGH_GREATERTHAN_TWO='fa_peg_high'
        UNDER_ONE='fa_peg_u1'
        UNDER_TWO='fa_peg_u2'
        UNDER_THREE='fa_peg_u3'
        OVER_ONE='fa_peg_o1'
        OVER_TWO='fa_peg_o2'
        OVER_THREE='fa_peg_o3'

    def filter_peg(self, peg: Peg):
        self.filters['Peg'] = peg

    class PS(str, Enum):
        """
        P/S number reflects the value placed on sales by the market. It is calculated by dividing the current closing price of the stock by the dollar-sales value per share.
        """
        LOW_LESSTHAN_ONE='fa_ps_low'
        HIGH_GREATERTHAN_TEN='fa_ps_high'
        UNDER_ONE='fa_ps_u1'
        UNDER_TWO='fa_ps_u2'
        UNDER_THREE='fa_ps_u3'
        UNDER_FOUR='fa_ps_u4'
        UNDER_FIVE='fa_ps_u5'
        UNDER_SIX='fa_ps_u6'
        UNDER_SEVEN='fa_ps_u7'
        UNDER_EIGHT='fa_ps_u8'
        UNDER_NINE='fa_ps_u9'
        UNDER_TEN='fa_ps_u10'
        OVER_ONE='fa_ps_o1'
        OVER_TWO='fa_ps_o2'
        OVER_THREE='fa_ps_o3'
        OVER_FOUR='fa_ps_o4'
        OVER_FIVE='fa_ps_o5'
        OVER_SIX='fa_ps_o6'
        OVER_SEVEN='fa_ps_o7'
        OVER_EIGHT='fa_ps_o8'
        OVER_NINE='fa_ps_o9'
        OVER_TEN='fa_ps_o10'

    def filter_p_s(self, p_s: PS):
        self.filters['PS'] = p_s

    class PB(str, Enum):
        """
        A ratio used to compare a stock's market value to its book value. It is calculated by dividing the current closing price of the stock by the latest quarter's book value per share.
        """
        LOW_LESSTHAN_ONE='fa_pb_low'
        HIGH_GREATERTHAN_FIVE='fa_pb_high'
        UNDER_ONE='fa_pb_u1'
        UNDER_TWO='fa_pb_u2'
        UNDER_THREE='fa_pb_u3'
        UNDER_FOUR='fa_pb_u4'
        UNDER_FIVE='fa_pb_u5'
        UNDER_SIX='fa_pb_u6'
        UNDER_SEVEN='fa_pb_u7'
        UNDER_EIGHT='fa_pb_u8'
        UNDER_NINE='fa_pb_u9'
        UNDER_TEN='fa_pb_u10'
        OVER_ONE='fa_pb_o1'
        OVER_TWO='fa_pb_o2'
        OVER_THREE='fa_pb_o3'
        OVER_FOUR='fa_pb_o4'
        OVER_FIVE='fa_pb_o5'
        OVER_SIX='fa_pb_o6'
        OVER_SEVEN='fa_pb_o7'
        OVER_EIGHT='fa_pb_o8'
        OVER_NINE='fa_pb_o9'
        OVER_TEN='fa_pb_o10'

    def filter_p_b(self, p_b: PB):
        self.filters['PB'] = p_b

    class PriceCash(str, Enum):
        """
        A ratio used to compare a stock's market value to its cash assets. It is calculated by dividing the current closing price of the stock by the latest quarter's cash per share.
        """
        LOW_LESSTHAN_THREE='fa_pc_low'
        HIGH_GREATERTHAN_FIFTY='fa_pc_high'
        UNDER_ONE='fa_pc_u1'
        UNDER_TWO='fa_pc_u2'
        UNDER_THREE='fa_pc_u3'
        UNDER_FOUR='fa_pc_u4'
        UNDER_FIVE='fa_pc_u5'
        UNDER_SIX='fa_pc_u6'
        UNDER_SEVEN='fa_pc_u7'
        UNDER_EIGHT='fa_pc_u8'
        UNDER_NINE='fa_pc_u9'
        UNDER_TEN='fa_pc_u10'
        OVER_ONE='fa_pc_o1'
        OVER_TWO='fa_pc_o2'
        OVER_THREE='fa_pc_o3'
        OVER_FOUR='fa_pc_o4'
        OVER_FIVE='fa_pc_o5'
        OVER_SIX='fa_pc_o6'
        OVER_SEVEN='fa_pc_o7'
        OVER_EIGHT='fa_pc_o8'
        OVER_NINE='fa_pc_o9'
        OVER_TEN='fa_pc_o10'
        OVER_TWENTY='fa_pc_o20'
        OVER_THIRTY='fa_pc_o30'
        OVER_FORTY='fa_pc_o40'
        OVER_FIFTY='fa_pc_o50'

    def filter_price_cash(self, price_cash: PriceCash):
        self.filters['PriceCash'] = price_cash

    class PriceFreeCashFlow(str, Enum):
        """
        A valuation metric that compares a company's market price to its level of annual free cash flow.
        """
        LOW_LESSTHAN_FIFTEEN='fa_pfcf_low'
        HIGH_GREATERTHAN_FIFTY='fa_pfcf_high'
        UNDER_FIVE='fa_pfcf_u5'
        UNDER_TEN='fa_pfcf_u10'
        UNDER_FIFTEEN='fa_pfcf_u15'
        UNDER_TWENTY='fa_pfcf_u20'
        UNDER_TWENTY_FIVE='fa_pfcf_u25'
        UNDER_THIRTY='fa_pfcf_u30'
        UNDER_THIRTY_FIVE='fa_pfcf_u35'
        UNDER_FORTY='fa_pfcf_u40'
        UNDER_FORTY_FIVE='fa_pfcf_u45'
        UNDER_FIFTY='fa_pfcf_u50'
        UNDER_SIXTY='fa_pfcf_u60'
        UNDER_SEVENTY='fa_pfcf_u70'
        UNDER_EIGHTY='fa_pfcf_u80'
        UNDER_NINETY='fa_pfcf_u90'
        UNDER_ONE_HUNDRED='fa_pfcf_u100'
        OVER_FIVE='fa_pfcf_o5'
        OVER_TEN='fa_pfcf_o10'
        OVER_FIFTEEN='fa_pfcf_o15'
        OVER_TWENTY='fa_pfcf_o20'
        OVER_TWENTY_FIVE='fa_pfcf_o25'
        OVER_THIRTY='fa_pfcf_o30'
        OVER_THIRTY_FIVE='fa_pfcf_o35'
        OVER_FORTY='fa_pfcf_o40'
        OVER_FORTY_FIVE='fa_pfcf_o45'
        OVER_FIFTY='fa_pfcf_o50'
        OVER_SIXTY='fa_pfcf_o60'
        OVER_SEVENTY='fa_pfcf_o70'
        OVER_EIGHTY='fa_pfcf_o80'
        OVER_NINETY='fa_pfcf_o90'
        OVER_ONE_HUNDRED='fa_pfcf_o100'

    def filter_price_free_cash_flow(self, price_free_cash_flow: PriceFreeCashFlow):
        self.filters['PriceFreeCashFlow'] = price_free_cash_flow

    class EpsGrowththisYear(str, Enum):
        """
        EPS is the portion of a company's profit allocated to each outstanding share of common stock. EPS serves as an indicator of a company's profitability.<br><br>Value for current fiscal year.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_epsyoy_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_epsyoy_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_epsyoy_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_epsyoy_high'
        UNDER_FIVE_PERCENT='fa_epsyoy_u5'
        UNDER_TEN_PERCENT='fa_epsyoy_u10'
        UNDER_FIFTEEN_PERCENT='fa_epsyoy_u15'
        UNDER_TWENTY_PERCENT='fa_epsyoy_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_epsyoy_u25'
        UNDER_THIRTY_PERCENT='fa_epsyoy_u30'
        OVER_FIVE_PERCENT='fa_epsyoy_o5'
        OVER_TEN_PERCENT='fa_epsyoy_o10'
        OVER_FIFTEEN_PERCENT='fa_epsyoy_o15'
        OVER_TWENTY_PERCENT='fa_epsyoy_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_epsyoy_o25'
        OVER_THIRTY_PERCENT='fa_epsyoy_o30'

    def filter_eps_growththis_year(self, eps_growththis_year: EpsGrowththisYear):
        self.filters['EpsGrowththisYear'] = eps_growththis_year

    class EpsGrowthnextYear(str, Enum):
        """
        EPS is the portion of a company's profit allocated to each outstanding share of common stock. EPS serves as an indicator of a company's profitability.<br><br>Estimate for next fiscal year.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_epsyoy1_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_epsyoy1_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_epsyoy1_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_epsyoy1_high'
        UNDER_FIVE_PERCENT='fa_epsyoy1_u5'
        UNDER_TEN_PERCENT='fa_epsyoy1_u10'
        UNDER_FIFTEEN_PERCENT='fa_epsyoy1_u15'
        UNDER_TWENTY_PERCENT='fa_epsyoy1_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_epsyoy1_u25'
        UNDER_THIRTY_PERCENT='fa_epsyoy1_u30'
        OVER_FIVE_PERCENT='fa_epsyoy1_o5'
        OVER_TEN_PERCENT='fa_epsyoy1_o10'
        OVER_FIFTEEN_PERCENT='fa_epsyoy1_o15'
        OVER_TWENTY_PERCENT='fa_epsyoy1_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_epsyoy1_o25'
        OVER_THIRTY_PERCENT='fa_epsyoy1_o30'

    def filter_eps_growthnext_year(self, eps_growthnext_year: EpsGrowthnextYear):
        self.filters['EpsGrowthnextYear'] = eps_growthnext_year

    class EpsGrowthpastFiveYears(str, Enum):
        """
        EPS is the portion of a company's profit allocated to each outstanding share of common stock. EPS serves as an indicator of a company's profitability.<br><br>Annual growth over past 5 years.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_eps5years_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_eps5years_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_eps5years_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_eps5years_high'
        UNDER_FIVE_PERCENT='fa_eps5years_u5'
        UNDER_TEN_PERCENT='fa_eps5years_u10'
        UNDER_FIFTEEN_PERCENT='fa_eps5years_u15'
        UNDER_TWENTY_PERCENT='fa_eps5years_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_eps5years_u25'
        UNDER_THIRTY_PERCENT='fa_eps5years_u30'
        OVER_FIVE_PERCENT='fa_eps5years_o5'
        OVER_TEN_PERCENT='fa_eps5years_o10'
        OVER_FIFTEEN_PERCENT='fa_eps5years_o15'
        OVER_TWENTY_PERCENT='fa_eps5years_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_eps5years_o25'
        OVER_THIRTY_PERCENT='fa_eps5years_o30'

    def filter_eps_growthpast_five_years(self, eps_growthpast_five_years: EpsGrowthpastFiveYears):
        self.filters['EpsGrowthpastFiveYears'] = eps_growthpast_five_years

    class EpsGrowthnextFiveYears(str, Enum):
        """
        EPS is the portion of a company's profit allocated to each outstanding share of common stock. EPS serves as an indicator of a company's profitability.<br><br>Long term annual growth estimate.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_estltgrowth_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_estltgrowth_pos'
        POSITIVE_LOW_LESSTHAN_TEN_PERCENT='fa_estltgrowth_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_estltgrowth_high'
        UNDER_FIVE_PERCENT='fa_estltgrowth_u5'
        UNDER_TEN_PERCENT='fa_estltgrowth_u10'
        UNDER_FIFTEEN_PERCENT='fa_estltgrowth_u15'
        UNDER_TWENTY_PERCENT='fa_estltgrowth_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_estltgrowth_u25'
        UNDER_THIRTY_PERCENT='fa_estltgrowth_u30'
        OVER_FIVE_PERCENT='fa_estltgrowth_o5'
        OVER_TEN_PERCENT='fa_estltgrowth_o10'
        OVER_FIFTEEN_PERCENT='fa_estltgrowth_o15'
        OVER_TWENTY_PERCENT='fa_estltgrowth_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_estltgrowth_o25'
        OVER_THIRTY_PERCENT='fa_estltgrowth_o30'

    def filter_eps_growthnext_five_years(self, eps_growthnext_five_years: EpsGrowthnextFiveYears):
        self.filters['EpsGrowthnextFiveYears'] = eps_growthnext_five_years

    class SalesGrowthpastFiveYears(str, Enum):
        """
        Annual growth over past 5 years.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_sales5years_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_sales5years_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_sales5years_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_sales5years_high'
        UNDER_FIVE_PERCENT='fa_sales5years_u5'
        UNDER_TEN_PERCENT='fa_sales5years_u10'
        UNDER_FIFTEEN_PERCENT='fa_sales5years_u15'
        UNDER_TWENTY_PERCENT='fa_sales5years_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_sales5years_u25'
        UNDER_THIRTY_PERCENT='fa_sales5years_u30'
        OVER_FIVE_PERCENT='fa_sales5years_o5'
        OVER_TEN_PERCENT='fa_sales5years_o10'
        OVER_FIFTEEN_PERCENT='fa_sales5years_o15'
        OVER_TWENTY_PERCENT='fa_sales5years_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_sales5years_o25'
        OVER_THIRTY_PERCENT='fa_sales5years_o30'

    def filter_sales_growthpast_five_years(self, sales_growthpast_five_years: SalesGrowthpastFiveYears):
        self.filters['SalesGrowthpastFiveYears'] = sales_growthpast_five_years

    class EpsGrowthqtrOverQtr(str, Enum):
        """
        EPS is the portion of a company's profit allocated to each outstanding share of common stock. EPS serves as an indicator of a company's profitability.<br><br>Quarter over quarter growth.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_epsqoq_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_epsqoq_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_epsqoq_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_epsqoq_high'
        UNDER_FIVE_PERCENT='fa_epsqoq_u5'
        UNDER_TEN_PERCENT='fa_epsqoq_u10'
        UNDER_FIFTEEN_PERCENT='fa_epsqoq_u15'
        UNDER_TWENTY_PERCENT='fa_epsqoq_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_epsqoq_u25'
        UNDER_THIRTY_PERCENT='fa_epsqoq_u30'
        OVER_FIVE_PERCENT='fa_epsqoq_o5'
        OVER_TEN_PERCENT='fa_epsqoq_o10'
        OVER_FIFTEEN_PERCENT='fa_epsqoq_o15'
        OVER_TWENTY_PERCENT='fa_epsqoq_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_epsqoq_o25'
        OVER_THIRTY_PERCENT='fa_epsqoq_o30'

    def filter_eps_growthqtr_over_qtr(self, eps_growthqtr_over_qtr: EpsGrowthqtrOverQtr):
        self.filters['EpsGrowthqtrOverQtr'] = eps_growthqtr_over_qtr

    class SalesGrowthqtrOverQtr(str, Enum):
        """
        Quarter over quarter growth compared on a year over year basis.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_salesqoq_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_salesqoq_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_salesqoq_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_salesqoq_high'
        UNDER_FIVE_PERCENT='fa_salesqoq_u5'
        UNDER_TEN_PERCENT='fa_salesqoq_u10'
        UNDER_FIFTEEN_PERCENT='fa_salesqoq_u15'
        UNDER_TWENTY_PERCENT='fa_salesqoq_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_salesqoq_u25'
        UNDER_THIRTY_PERCENT='fa_salesqoq_u30'
        OVER_FIVE_PERCENT='fa_salesqoq_o5'
        OVER_TEN_PERCENT='fa_salesqoq_o10'
        OVER_FIFTEEN_PERCENT='fa_salesqoq_o15'
        OVER_TWENTY_PERCENT='fa_salesqoq_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_salesqoq_o25'
        OVER_THIRTY_PERCENT='fa_salesqoq_o30'

    def filter_sales_growthqtr_over_qtr(self, sales_growthqtr_over_qtr: SalesGrowthqtrOverQtr):
        self.filters['SalesGrowthqtrOverQtr'] = sales_growthqtr_over_qtr

    class EpsGrowthTtm(str, Enum):
        """
        Trailing twelve months growth compared on the previous audited financial year.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_epsyoyttm_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_epsyoyttm_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_epsyoyttm_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_epsyoyttm_high'
        UNDER_FIVE_PERCENT='fa_epsyoyttm_u5'
        UNDER_TEN_PERCENT='fa_epsyoyttm_u10'
        UNDER_FIFTEEN_PERCENT='fa_epsyoyttm_u15'
        UNDER_TWENTY_PERCENT='fa_epsyoyttm_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_epsyoyttm_u25'
        UNDER_THIRTY_PERCENT='fa_epsyoyttm_u30'
        OVER_FIVE_PERCENT='fa_epsyoyttm_o5'
        OVER_TEN_PERCENT='fa_epsyoyttm_o10'
        OVER_FIFTEEN_PERCENT='fa_epsyoyttm_o15'
        OVER_TWENTY_PERCENT='fa_epsyoyttm_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_epsyoyttm_o25'
        OVER_THIRTY_PERCENT='fa_epsyoyttm_o30'

    def filter_eps_growth_ttm(self, eps_growth_ttm: EpsGrowthTtm):
        self.filters['EpsGrowthTtm'] = eps_growth_ttm

    class SalesGrowthTtm(str, Enum):
        """
        Trailing twelve months growth compared on the previous audited financial year.
        """
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_salesyoyttm_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_salesyoyttm_pos'
        POSITIVE_LOW_ZERO_TEN_PERCENT='fa_salesyoyttm_poslow'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_salesyoyttm_high'
        UNDER_FIVE_PERCENT='fa_salesyoyttm_u5'
        UNDER_TEN_PERCENT='fa_salesyoyttm_u10'
        UNDER_FIFTEEN_PERCENT='fa_salesyoyttm_u15'
        UNDER_TWENTY_PERCENT='fa_salesyoyttm_u20'
        UNDER_TWENTY_FIVE_PERCENT='fa_salesyoyttm_u25'
        UNDER_THIRTY_PERCENT='fa_salesyoyttm_u30'
        OVER_FIVE_PERCENT='fa_salesyoyttm_o5'
        OVER_TEN_PERCENT='fa_salesyoyttm_o10'
        OVER_FIFTEEN_PERCENT='fa_salesyoyttm_o15'
        OVER_TWENTY_PERCENT='fa_salesyoyttm_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_salesyoyttm_o25'
        OVER_THIRTY_PERCENT='fa_salesyoyttm_o30'

    def filter_sales_growth_ttm(self, sales_growth_ttm: SalesGrowthTtm):
        self.filters['SalesGrowthTtm'] = sales_growth_ttm

    class EarningsAndRevenueSurprise(str, Enum):
        """
        Company's reported earnings/revenue are above or below analysts' expectations.
        """
        BOTH_POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_epsrev_bp'
        BOTH_MET_ZERO_PERCENT='fa_epsrev_bm'
        BOTH_NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_epsrev_bn'

    def filter_earnings_and_revenue_surprise(self, earnings_and_revenue_surprise: EarningsAndRevenueSurprise):
        self.filters['EarningsAndRevenueSurprise'] = earnings_and_revenue_surprise

    class DividendYield(str, Enum):
        """
        The dividend yield equals the annual dividend per share divided by the stock’s price. This measurement tells what percentage return a company pays out to shareholders in the form of dividends.<br><br>If there is no forward dividend estimate available, trailing twelve month (TTM) value is used.<br>
        """
        NONE_ZERO_PERCENT='fa_div_none'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_div_pos'
        HIGH_GREATERTHAN_FIVE_PERCENT='fa_div_high'
        VERY_HIGH_GREATERTHAN_TEN_PERCENT='fa_div_veryhigh'
        OVER_ONE_PERCENT='fa_div_o1'
        OVER_TWO_PERCENT='fa_div_o2'
        OVER_THREE_PERCENT='fa_div_o3'
        OVER_FOUR_PERCENT='fa_div_o4'
        OVER_FIVE_PERCENT='fa_div_o5'
        OVER_SIX_PERCENT='fa_div_o6'
        OVER_SEVEN_PERCENT='fa_div_o7'
        OVER_EIGHT_PERCENT='fa_div_o8'
        OVER_NINE_PERCENT='fa_div_o9'
        OVER_TEN_PERCENT='fa_div_o10'

    def filter_dividend_yield(self, dividend_yield: DividendYield):
        self.filters['DividendYield'] = dividend_yield

    class ReturnOnAssets(str, Enum):
        """
        An indicator of how profitable a company is relative to its total assets. ROA gives an idea as to how efficient management is at using its assets to generate earnings. Calculated by dividing a company's annual earnings by its total assets, ROA is displayed as a percentage.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_roa_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_roa_neg'
        VERY_POSITIVE_GREATERTHAN_FIFTEEN_PERCENT='fa_roa_verypos'
        VERY_NEGATIVE_LESSTHAN_FIFTEEN_PERCENT='fa_roa_veryneg'
        UNDER_FIFTY_PERCENT='fa_roa_u-50'
        UNDER_FORTY_FIVE_PERCENT='fa_roa_u-45'
        UNDER_FORTY_PERCENT='fa_roa_u-40'
        UNDER_THIRTY_FIVE_PERCENT='fa_roa_u-35'
        UNDER_THIRTY_PERCENT='fa_roa_u-30'
        UNDER_TWENTY_FIVE_PERCENT='fa_roa_u-25'
        UNDER_TWENTY_PERCENT='fa_roa_u-20'
        UNDER_FIFTEEN_PERCENT='fa_roa_u-15'
        UNDER_TEN_PERCENT='fa_roa_u-10'
        UNDER_FIVE_PERCENT='fa_roa_u-5'
        OVER_PLUS_FIVE_PERCENT='fa_roa_o5'
        OVER_PLUS_TEN_PERCENT='fa_roa_o10'
        OVER_PLUS_FIFTEEN_PERCENT='fa_roa_o15'
        OVER_PLUS_TWENTY_PERCENT='fa_roa_o20'
        OVER_PLUS_TWENTY_FIVE_PERCENT='fa_roa_o25'
        OVER_PLUS_THIRTY_PERCENT='fa_roa_o30'
        OVER_PLUS_THIRTY_FIVE_PERCENT='fa_roa_o35'
        OVER_PLUS_FORTY_PERCENT='fa_roa_o40'
        OVER_PLUS_FORTY_FIVE_PERCENT='fa_roa_o45'
        OVER_PLUS_FIFTY_PERCENT='fa_roa_o50'

    def filter_return_on_assets(self, return_on_assets: ReturnOnAssets):
        self.filters['ReturnOnAssets'] = return_on_assets

    class ReturnOnEquity(str, Enum):
        """
        A measure of a corporation's profitability that reveals how much profit a company generates with the money shareholders have invested. Calculated as Net Income / Shareholder's Equity.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_roe_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_roe_neg'
        VERY_POSITIVE_GREATERTHAN_THIRTY_PERCENT='fa_roe_verypos'
        VERY_NEGATIVE_LESSTHAN_FIFTEEN_PERCENT='fa_roe_veryneg'
        UNDER_FIFTY_PERCENT='fa_roe_u-50'
        UNDER_FORTY_FIVE_PERCENT='fa_roe_u-45'
        UNDER_FORTY_PERCENT='fa_roe_u-40'
        UNDER_THIRTY_FIVE_PERCENT='fa_roe_u-35'
        UNDER_THIRTY_PERCENT='fa_roe_u-30'
        UNDER_TWENTY_FIVE_PERCENT='fa_roe_u-25'
        UNDER_TWENTY_PERCENT='fa_roe_u-20'
        UNDER_FIFTEEN_PERCENT='fa_roe_u-15'
        UNDER_TEN_PERCENT='fa_roe_u-10'
        UNDER_FIVE_PERCENT='fa_roe_u-5'
        OVER_PLUS_FIVE_PERCENT='fa_roe_o5'
        OVER_PLUS_TEN_PERCENT='fa_roe_o10'
        OVER_PLUS_FIFTEEN_PERCENT='fa_roe_o15'
        OVER_PLUS_TWENTY_PERCENT='fa_roe_o20'
        OVER_PLUS_TWENTY_FIVE_PERCENT='fa_roe_o25'
        OVER_PLUS_THIRTY_PERCENT='fa_roe_o30'
        OVER_PLUS_THIRTY_FIVE_PERCENT='fa_roe_o35'
        OVER_PLUS_FORTY_PERCENT='fa_roe_o40'
        OVER_PLUS_FORTY_FIVE_PERCENT='fa_roe_o45'
        OVER_PLUS_FIFTY_PERCENT='fa_roe_o50'

    def filter_return_on_equity(self, return_on_equity: ReturnOnEquity):
        self.filters['ReturnOnEquity'] = return_on_equity

    class ReturnOnInvestedCapital(str, Enum):
        """
        A financial metric used to measure a company's efficiency in allocating its capital to generate returns. It assesses how well a company is using its resources to create value for its investors. ROIC is particularly useful for evaluating a company's profitability and its ability to sustain competitive advantages over time. ROIC is calculated as Net Income / Invested Capital.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_roi_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_roi_neg'
        VERY_POSITIVE_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_roi_verypos'
        VERY_NEGATIVE_LESSTHAN_TEN_PERCENT='fa_roi_veryneg'
        UNDER_FIFTY_PERCENT='fa_roi_u-50'
        UNDER_FORTY_FIVE_PERCENT='fa_roi_u-45'
        UNDER_FORTY_PERCENT='fa_roi_u-40'
        UNDER_THIRTY_FIVE_PERCENT='fa_roi_u-35'
        UNDER_THIRTY_PERCENT='fa_roi_u-30'
        UNDER_TWENTY_FIVE_PERCENT='fa_roi_u-25'
        UNDER_TWENTY_PERCENT='fa_roi_u-20'
        UNDER_FIFTEEN_PERCENT='fa_roi_u-15'
        UNDER_TEN_PERCENT='fa_roi_u-10'
        UNDER_FIVE_PERCENT='fa_roi_u-5'
        OVER_PLUS_FIVE_PERCENT='fa_roi_o5'
        OVER_PLUS_TEN_PERCENT='fa_roi_o10'
        OVER_PLUS_FIFTEEN_PERCENT='fa_roi_o15'
        OVER_PLUS_TWENTY_PERCENT='fa_roi_o20'
        OVER_PLUS_TWENTY_FIVE_PERCENT='fa_roi_o25'
        OVER_PLUS_THIRTY_PERCENT='fa_roi_o30'
        OVER_PLUS_THIRTY_FIVE_PERCENT='fa_roi_o35'
        OVER_PLUS_FORTY_PERCENT='fa_roi_o40'
        OVER_PLUS_FORTY_FIVE_PERCENT='fa_roi_o45'
        OVER_PLUS_FIFTY_PERCENT='fa_roi_o50'

    def filter_return_on_invested_capital(self, return_on_invested_capital: ReturnOnInvestedCapital):
        self.filters['ReturnOnInvestedCapital'] = return_on_invested_capital

    class CurrentRatio(str, Enum):
        """
        A liquidity ratio that measures a company's ability to pay short-term obligations. Calculated as Current Assets / Current Liabilities.
        """
        HIGH_GREATERTHAN_THREE='fa_curratio_high'
        LOW_LESSTHAN_ONE='fa_curratio_low'
        UNDER_ONE='fa_curratio_u1'
        UNDER_ZERO_FIVE='fa_curratio_u0.5'
        OVER_ZERO_FIVE='fa_curratio_o0.5'
        OVER_ONE='fa_curratio_o1'
        OVER_ONE_FIVE='fa_curratio_o1.5'
        OVER_TWO='fa_curratio_o2'
        OVER_THREE='fa_curratio_o3'
        OVER_FOUR='fa_curratio_o4'
        OVER_FIVE='fa_curratio_o5'
        OVER_TEN='fa_curratio_o10'

    def filter_current_ratio(self, current_ratio: CurrentRatio):
        self.filters['CurrentRatio'] = current_ratio

    class QuickRatio(str, Enum):
        """
        An indicator of a company's short-term liquidity. The quick ratio measures a company's ability to meet its short-term obligations with its most liquid assets. The higher the quick ratio, the better the position of the company. Calculated as (Current Assets - Inventories) / Current Liabilities.
        """
        HIGH_GREATERTHAN_THREE='fa_quickratio_high'
        LOW_LESSTHAN_ZERO_FIVE='fa_quickratio_low'
        UNDER_ONE='fa_quickratio_u1'
        UNDER_ZERO_FIVE='fa_quickratio_u0.5'
        OVER_ZERO_FIVE='fa_quickratio_o0.5'
        OVER_ONE='fa_quickratio_o1'
        OVER_ONE_FIVE='fa_quickratio_o1.5'
        OVER_TWO='fa_quickratio_o2'
        OVER_THREE='fa_quickratio_o3'
        OVER_FOUR='fa_quickratio_o4'
        OVER_FIVE='fa_quickratio_o5'
        OVER_TEN='fa_quickratio_o10'

    def filter_quick_ratio(self, quick_ratio: QuickRatio):
        self.filters['QuickRatio'] = quick_ratio

    class LtDebtEquity(str, Enum):
        """
        A measure of a company's financial leverage calculated by dividing its long term debt by stockholders' equity. It indicates what proportion of equity and debt the company is using to finance its assets.
        """
        HIGH_GREATERTHAN_ZERO_FIVE='fa_ltdebteq_high'
        LOW_LESSTHAN_ZERO_ONE='fa_ltdebteq_low'
        UNDER_ONE='fa_ltdebteq_u1'
        UNDER_ZERO_NINE='fa_ltdebteq_u0.9'
        UNDER_ZERO_EIGHT='fa_ltdebteq_u0.8'
        UNDER_ZERO_SEVEN='fa_ltdebteq_u0.7'
        UNDER_ZERO_SIX='fa_ltdebteq_u0.6'
        UNDER_ZERO_FIVE='fa_ltdebteq_u0.5'
        UNDER_ZERO_FOUR='fa_ltdebteq_u0.4'
        UNDER_ZERO_THREE='fa_ltdebteq_u0.3'
        UNDER_ZERO_TWO='fa_ltdebteq_u0.2'
        UNDER_ZERO_ONE='fa_ltdebteq_u0.1'
        OVER_ZERO_ONE='fa_ltdebteq_o0.1'
        OVER_ZERO_TWO='fa_ltdebteq_o0.2'
        OVER_ZERO_THREE='fa_ltdebteq_o0.3'
        OVER_ZERO_FOUR='fa_ltdebteq_o0.4'
        OVER_ZERO_FIVE='fa_ltdebteq_o0.5'
        OVER_ZERO_SIX='fa_ltdebteq_o0.6'
        OVER_ZERO_SEVEN='fa_ltdebteq_o0.7'
        OVER_ZERO_EIGHT='fa_ltdebteq_o0.8'
        OVER_ZERO_NINE='fa_ltdebteq_o0.9'
        OVER_ONE='fa_ltdebteq_o1'

    def filter_lt_debt_equity(self, lt_debt_equity: LtDebtEquity):
        self.filters['LtDebtEquity'] = lt_debt_equity

    class DebtEquity(str, Enum):
        """
        A measure of a company's financial leverage calculated by dividing its liabilities by stockholders' equity. It indicates what proportion of equity and debt the company is using to finance its assets.
        """
        HIGH_GREATERTHAN_ZERO_FIVE='fa_debteq_high'
        LOW_LESSTHAN_ZERO_ONE='fa_debteq_low'
        UNDER_ONE='fa_debteq_u1'
        UNDER_ZERO_NINE='fa_debteq_u0.9'
        UNDER_ZERO_EIGHT='fa_debteq_u0.8'
        UNDER_ZERO_SEVEN='fa_debteq_u0.7'
        UNDER_ZERO_SIX='fa_debteq_u0.6'
        UNDER_ZERO_FIVE='fa_debteq_u0.5'
        UNDER_ZERO_FOUR='fa_debteq_u0.4'
        UNDER_ZERO_THREE='fa_debteq_u0.3'
        UNDER_ZERO_TWO='fa_debteq_u0.2'
        UNDER_ZERO_ONE='fa_debteq_u0.1'
        OVER_ZERO_ONE='fa_debteq_o0.1'
        OVER_ZERO_TWO='fa_debteq_o0.2'
        OVER_ZERO_THREE='fa_debteq_o0.3'
        OVER_ZERO_FOUR='fa_debteq_o0.4'
        OVER_ZERO_FIVE='fa_debteq_o0.5'
        OVER_ZERO_SIX='fa_debteq_o0.6'
        OVER_ZERO_SEVEN='fa_debteq_o0.7'
        OVER_ZERO_EIGHT='fa_debteq_o0.8'
        OVER_ZERO_NINE='fa_debteq_o0.9'
        OVER_ONE='fa_debteq_o1'

    def filter_debt_equity(self, debt_equity: DebtEquity):
        self.filters['DebtEquity'] = debt_equity

    class GrossMargin(str, Enum):
        """
        A company's total sales revenue minus its cost of goods sold, divided by the total sales revenue, expressed as a percentage. The gross margin represents the percent of total sales revenue that the company retains after incurring the direct costs associated with producing the goods and services sold by a company. The higher the percentage, the more the company retains on each dollar of sales to service its other costs and obligations.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_grossmargin_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_grossmargin_neg'
        HIGH_GREATERTHAN_FIFTY_PERCENT='fa_grossmargin_high'
        UNDER_NINETY_PERCENT='fa_grossmargin_u90'
        UNDER_EIGHTY_PERCENT='fa_grossmargin_u80'
        UNDER_SEVENTY_PERCENT='fa_grossmargin_u70'
        UNDER_SIXTY_PERCENT='fa_grossmargin_u60'
        UNDER_FIFTY_PERCENT='fa_grossmargin_u50'
        UNDER_FORTY_FIVE_PERCENT='fa_grossmargin_u45'
        UNDER_FORTY_PERCENT='fa_grossmargin_u40'
        UNDER_THIRTY_FIVE_PERCENT='fa_grossmargin_u35'
        UNDER_THIRTY_PERCENT='fa_grossmargin_u30'
        UNDER_TWENTY_FIVE_PERCENT='fa_grossmargin_u25'
        UNDER_TWENTY_PERCENT='fa_grossmargin_u20'
        UNDER_FIFTEEN_PERCENT='fa_grossmargin_u15'
        UNDER_TEN_PERCENT='fa_grossmargin_u10'
        UNDER_FIVE_PERCENT='fa_grossmargin_u5'
        UNDER_ZERO_PERCENT='fa_grossmargin_u0'
        UNDER_ONE_HUNDRED_PERCENT='fa_grossmargin_u-100'
        OVER_ZERO_PERCENT='fa_grossmargin_o0'
        OVER_FIVE_PERCENT='fa_grossmargin_o5'
        OVER_TEN_PERCENT='fa_grossmargin_o10'
        OVER_FIFTEEN_PERCENT='fa_grossmargin_o15'
        OVER_TWENTY_PERCENT='fa_grossmargin_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_grossmargin_o25'
        OVER_THIRTY_PERCENT='fa_grossmargin_o30'
        OVER_THIRTY_FIVE_PERCENT='fa_grossmargin_o35'
        OVER_FORTY_PERCENT='fa_grossmargin_o40'
        OVER_FORTY_FIVE_PERCENT='fa_grossmargin_o45'
        OVER_FIFTY_PERCENT='fa_grossmargin_o50'
        OVER_SIXTY_PERCENT='fa_grossmargin_o60'
        OVER_SEVENTY_PERCENT='fa_grossmargin_o70'
        OVER_EIGHTY_PERCENT='fa_grossmargin_o80'
        OVER_NINETY_PERCENT='fa_grossmargin_o90'

    def filter_gross_margin(self, gross_margin: GrossMargin):
        self.filters['GrossMargin'] = gross_margin

    class OperatingMargin(str, Enum):
        """
        Operating margin is a measurement of what proportion of a company's revenue is left over after paying for variable costs of production such as wages, raw materials, etc. A healthy operating margin is required for a company to be able to pay for its fixed costs, such as interest on debt. Calculated as Operating Income / Net Sales.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_opermargin_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_opermargin_neg'
        VERY_NEGATIVE_LESSTHAN_TWENTY_PERCENT='fa_opermargin_veryneg'
        HIGH_GREATERTHAN_TWENTY_FIVE_PERCENT='fa_opermargin_high'
        UNDER_NINETY_PERCENT='fa_opermargin_u90'
        UNDER_EIGHTY_PERCENT='fa_opermargin_u80'
        UNDER_SEVENTY_PERCENT='fa_opermargin_u70'
        UNDER_SIXTY_PERCENT='fa_opermargin_u60'
        UNDER_FIFTY_PERCENT='fa_opermargin_u50'
        UNDER_FORTY_FIVE_PERCENT='fa_opermargin_u45'
        UNDER_FORTY_PERCENT='fa_opermargin_u40'
        UNDER_THIRTY_FIVE_PERCENT='fa_opermargin_u35'
        UNDER_THIRTY_PERCENT='fa_opermargin_u30'
        UNDER_TWENTY_FIVE_PERCENT='fa_opermargin_u25'
        UNDER_TWENTY_PERCENT='fa_opermargin_u20'
        UNDER_FIFTEEN_PERCENT='fa_opermargin_u15'
        UNDER_TEN_PERCENT='fa_opermargin_u10'
        UNDER_FIVE_PERCENT='fa_opermargin_u5'
        UNDER_ZERO_PERCENT='fa_opermargin_u0'
        UNDER_ONE_HUNDRED_PERCENT='fa_opermargin_u-100'
        OVER_ZERO_PERCENT='fa_opermargin_o0'
        OVER_FIVE_PERCENT='fa_opermargin_o5'
        OVER_TEN_PERCENT='fa_opermargin_o10'
        OVER_FIFTEEN_PERCENT='fa_opermargin_o15'
        OVER_TWENTY_PERCENT='fa_opermargin_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_opermargin_o25'
        OVER_THIRTY_PERCENT='fa_opermargin_o30'
        OVER_THIRTY_FIVE_PERCENT='fa_opermargin_o35'
        OVER_FORTY_PERCENT='fa_opermargin_o40'
        OVER_FORTY_FIVE_PERCENT='fa_opermargin_o45'
        OVER_FIFTY_PERCENT='fa_opermargin_o50'
        OVER_SIXTY_PERCENT='fa_opermargin_o60'
        OVER_SEVENTY_PERCENT='fa_opermargin_o70'
        OVER_EIGHTY_PERCENT='fa_opermargin_o80'
        OVER_NINETY_PERCENT='fa_opermargin_o90'

    def filter_operating_margin(self, operating_margin: OperatingMargin):
        self.filters['OperatingMargin'] = operating_margin

    class NetProfitMargin(str, Enum):
        """
        A ratio of profitability calculated as net income divided by revenues, or net profits divided by sales. It measures how much out of every dollar of sales a company actually keeps in earnings.
        """
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_netmargin_pos'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='fa_netmargin_neg'
        VERY_NEGATIVE_LESSTHAN_TWENTY_PERCENT='fa_netmargin_veryneg'
        HIGH_GREATERTHAN_TWENTY_PERCENT='fa_netmargin_high'
        UNDER_NINETY_PERCENT='fa_netmargin_u90'
        UNDER_EIGHTY_PERCENT='fa_netmargin_u80'
        UNDER_SEVENTY_PERCENT='fa_netmargin_u70'
        UNDER_SIXTY_PERCENT='fa_netmargin_u60'
        UNDER_FIFTY_PERCENT='fa_netmargin_u50'
        UNDER_FORTY_FIVE_PERCENT='fa_netmargin_u45'
        UNDER_FORTY_PERCENT='fa_netmargin_u40'
        UNDER_THIRTY_FIVE_PERCENT='fa_netmargin_u35'
        UNDER_THIRTY_PERCENT='fa_netmargin_u30'
        UNDER_TWENTY_FIVE_PERCENT='fa_netmargin_u25'
        UNDER_TWENTY_PERCENT='fa_netmargin_u20'
        UNDER_FIFTEEN_PERCENT='fa_netmargin_u15'
        UNDER_TEN_PERCENT='fa_netmargin_u10'
        UNDER_FIVE_PERCENT='fa_netmargin_u5'
        UNDER_ZERO_PERCENT='fa_netmargin_u0'
        UNDER_ONE_HUNDRED_PERCENT='fa_netmargin_u-100'
        OVER_ZERO_PERCENT='fa_netmargin_o0'
        OVER_FIVE_PERCENT='fa_netmargin_o5'
        OVER_TEN_PERCENT='fa_netmargin_o10'
        OVER_FIFTEEN_PERCENT='fa_netmargin_o15'
        OVER_TWENTY_PERCENT='fa_netmargin_o20'
        OVER_TWENTY_FIVE_PERCENT='fa_netmargin_o25'
        OVER_THIRTY_PERCENT='fa_netmargin_o30'
        OVER_THIRTY_FIVE_PERCENT='fa_netmargin_o35'
        OVER_FORTY_PERCENT='fa_netmargin_o40'
        OVER_FORTY_FIVE_PERCENT='fa_netmargin_o45'
        OVER_FIFTY_PERCENT='fa_netmargin_o50'
        OVER_SIXTY_PERCENT='fa_netmargin_o60'
        OVER_SEVENTY_PERCENT='fa_netmargin_o70'
        OVER_EIGHTY_PERCENT='fa_netmargin_o80'
        OVER_NINETY_PERCENT='fa_netmargin_o90'

    def filter_net_profit_margin(self, net_profit_margin: NetProfitMargin):
        self.filters['NetProfitMargin'] = net_profit_margin

    class PayoutRatio(str, Enum):
        """
        The percentage of earnings paid to shareholders in dividends.
        """
        NONE_ZERO_PERCENT='fa_payoutratio_none'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='fa_payoutratio_pos'
        LOW_LESSTHAN_TWENTY_PERCENT='fa_payoutratio_low'
        HIGH_GREATERTHAN_FIFTY_PERCENT='fa_payoutratio_high'
        OVER_ZERO_PERCENT='fa_payoutratio_o0'
        OVER_TEN_PERCENT='fa_payoutratio_o10'
        OVER_TWENTY_PERCENT='fa_payoutratio_o20'
        OVER_THIRTY_PERCENT='fa_payoutratio_o30'
        OVER_FORTY_PERCENT='fa_payoutratio_o40'
        OVER_FIFTY_PERCENT='fa_payoutratio_o50'
        OVER_SIXTY_PERCENT='fa_payoutratio_o60'
        OVER_SEVENTY_PERCENT='fa_payoutratio_o70'
        OVER_EIGHTY_PERCENT='fa_payoutratio_o80'
        OVER_NINETY_PERCENT='fa_payoutratio_o90'
        OVER_ONE_HUNDRED_PERCENT='fa_payoutratio_o100'
        UNDER_TEN_PERCENT='fa_payoutratio_u10'
        UNDER_TWENTY_PERCENT='fa_payoutratio_u20'
        UNDER_THIRTY_PERCENT='fa_payoutratio_u30'
        UNDER_FORTY_PERCENT='fa_payoutratio_u40'
        UNDER_FIFTY_PERCENT='fa_payoutratio_u50'
        UNDER_SIXTY_PERCENT='fa_payoutratio_u60'
        UNDER_SEVENTY_PERCENT='fa_payoutratio_u70'
        UNDER_EIGHTY_PERCENT='fa_payoutratio_u80'
        UNDER_NINETY_PERCENT='fa_payoutratio_u90'
        UNDER_ONE_HUNDRED_PERCENT='fa_payoutratio_u100'

    def filter_payout_ratio(self, payout_ratio: PayoutRatio):
        self.filters['PayoutRatio'] = payout_ratio

    class Insiderownership(str, Enum):
        """
        Level to which a company is owned by its own management.
        """
        LOW_LESSTHAN_FIVE_PERCENT='sh_insiderown_low'
        HIGH_GREATERTHAN_THIRTY_PERCENT='sh_insiderown_high'
        VERY_HIGH_GREATERTHAN_FIFTY_PERCENT='sh_insiderown_veryhigh'
        OVER_TEN_PERCENT='sh_insiderown_o10'
        OVER_TWENTY_PERCENT='sh_insiderown_o20'
        OVER_THIRTY_PERCENT='sh_insiderown_o30'
        OVER_FORTY_PERCENT='sh_insiderown_o40'
        OVER_FIFTY_PERCENT='sh_insiderown_o50'
        OVER_SIXTY_PERCENT='sh_insiderown_o60'
        OVER_SEVENTY_PERCENT='sh_insiderown_o70'
        OVER_EIGHTY_PERCENT='sh_insiderown_o80'
        OVER_NINETY_PERCENT='sh_insiderown_o90'

    def filter_insiderownership(self, insiderownership: Insiderownership):
        self.filters['Insiderownership'] = insiderownership

    class Insidertransactions(str, Enum):
        """
        A company's shares being purchased or sold by its own management. Value represents 6-month percentual change in total insider ownership.
        """
        VERY_NEGATIVE_LESSTHAN_TWENTY_PERCENT='sh_insidertrans_veryneg'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='sh_insidertrans_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='sh_insidertrans_pos'
        VERY_POSITIVE_GREATERTHAN_TWENTY_PERCENT='sh_insidertrans_verypos'
        UNDER_NINETY_PERCENT='sh_insidertrans_u-90'
        UNDER_EIGHTY_PERCENT='sh_insidertrans_u-80'
        UNDER_SEVENTY_PERCENT='sh_insidertrans_u-70'
        UNDER_SIXTY_PERCENT='sh_insidertrans_u-60'
        UNDER_FIFTY_PERCENT='sh_insidertrans_u-50'
        UNDER_FORTY_FIVE_PERCENT='sh_insidertrans_u-45'
        UNDER_FORTY_PERCENT='sh_insidertrans_u-40'
        UNDER_THIRTY_FIVE_PERCENT='sh_insidertrans_u-35'
        UNDER_THIRTY_PERCENT='sh_insidertrans_u-30'
        UNDER_TWENTY_FIVE_PERCENT='sh_insidertrans_u-25'
        UNDER_TWENTY_PERCENT='sh_insidertrans_u-20'
        UNDER_FIFTEEN_PERCENT='sh_insidertrans_u-15'
        UNDER_TEN_PERCENT='sh_insidertrans_u-10'
        UNDER_FIVE_PERCENT='sh_insidertrans_u-5'
        OVER_PLUS_FIVE_PERCENT='sh_insidertrans_o5'
        OVER_PLUS_TEN_PERCENT='sh_insidertrans_o10'
        OVER_PLUS_FIFTEEN_PERCENT='sh_insidertrans_o15'
        OVER_PLUS_TWENTY_PERCENT='sh_insidertrans_o20'
        OVER_PLUS_TWENTY_FIVE_PERCENT='sh_insidertrans_o25'
        OVER_PLUS_THIRTY_PERCENT='sh_insidertrans_o30'
        OVER_PLUS_THIRTY_FIVE_PERCENT='sh_insidertrans_o35'
        OVER_PLUS_FORTY_PERCENT='sh_insidertrans_o40'
        OVER_PLUS_FORTY_FIVE_PERCENT='sh_insidertrans_o45'
        OVER_PLUS_FIFTY_PERCENT='sh_insidertrans_o50'
        OVER_PLUS_SIXTY_PERCENT='sh_insidertrans_o60'
        OVER_PLUS_SEVENTY_PERCENT='sh_insidertrans_o70'
        OVER_PLUS_EIGHTY_PERCENT='sh_insidertrans_o80'
        OVER_PLUS_NINETY_PERCENT='sh_insidertrans_o90'

    def filter_insidertransactions(self, insidertransactions: Insidertransactions):
        self.filters['Insidertransactions'] = insidertransactions

    class Institutionalownership(str, Enum):
        """
        Level to which a company is owned by financial institutions.
        """
        LOW_LESSTHAN_FIVE_PERCENT='sh_instown_low'
        HIGH_GREATERTHAN_NINETY_PERCENT='sh_instown_high'
        UNDER_NINETY_PERCENT='sh_instown_u90'
        UNDER_EIGHTY_PERCENT='sh_instown_u80'
        UNDER_SEVENTY_PERCENT='sh_instown_u70'
        UNDER_SIXTY_PERCENT='sh_instown_u60'
        UNDER_FIFTY_PERCENT='sh_instown_u50'
        UNDER_FORTY_PERCENT='sh_instown_u40'
        UNDER_THIRTY_PERCENT='sh_instown_u30'
        UNDER_TWENTY_PERCENT='sh_instown_u20'
        UNDER_TEN_PERCENT='sh_instown_u10'
        OVER_TEN_PERCENT='sh_instown_o10'
        OVER_TWENTY_PERCENT='sh_instown_o20'
        OVER_THIRTY_PERCENT='sh_instown_o30'
        OVER_FORTY_PERCENT='sh_instown_o40'
        OVER_FIFTY_PERCENT='sh_instown_o50'
        OVER_SIXTY_PERCENT='sh_instown_o60'
        OVER_SEVENTY_PERCENT='sh_instown_o70'
        OVER_EIGHTY_PERCENT='sh_instown_o80'
        OVER_NINETY_PERCENT='sh_instown_o90'

    def filter_institutionalownership(self, institutionalownership: Institutionalownership):
        self.filters['Institutionalownership'] = institutionalownership

    class Institutionaltransactions(str, Enum):
        """
        A company's shares being purchased or sold by financial institutions. Value represents 3-month change in institutional ownership.
        """
        VERY_NEGATIVE_LESSTHAN_TWENTY_PERCENT='sh_insttrans_veryneg'
        NEGATIVE_LESSTHAN_ZERO_PERCENT='sh_insttrans_neg'
        POSITIVE_GREATERTHAN_ZERO_PERCENT='sh_insttrans_pos'
        VERY_POSITIVE_GREATERTHAN_TWENTY_PERCENT='sh_insttrans_verypos'
        UNDER_FIFTY_PERCENT='sh_insttrans_u-50'
        UNDER_FORTY_FIVE_PERCENT='sh_insttrans_u-45'
        UNDER_FORTY_PERCENT='sh_insttrans_u-40'
        UNDER_THIRTY_FIVE_PERCENT='sh_insttrans_u-35'
        UNDER_THIRTY_PERCENT='sh_insttrans_u-30'
        UNDER_TWENTY_FIVE_PERCENT='sh_insttrans_u-25'
        UNDER_TWENTY_PERCENT='sh_insttrans_u-20'
        UNDER_FIFTEEN_PERCENT='sh_insttrans_u-15'
        UNDER_TEN_PERCENT='sh_insttrans_u-10'
        UNDER_FIVE_PERCENT='sh_insttrans_u-5'
        OVER_PLUS_FIVE_PERCENT='sh_insttrans_o5'
        OVER_PLUS_TEN_PERCENT='sh_insttrans_o10'
        OVER_PLUS_FIFTEEN_PERCENT='sh_insttrans_o15'
        OVER_PLUS_TWENTY_PERCENT='sh_insttrans_o20'
        OVER_PLUS_TWENTY_FIVE_PERCENT='sh_insttrans_o25'
        OVER_PLUS_THIRTY_PERCENT='sh_insttrans_o30'
        OVER_PLUS_THIRTY_FIVE_PERCENT='sh_insttrans_o35'
        OVER_PLUS_FORTY_PERCENT='sh_insttrans_o40'
        OVER_PLUS_FORTY_FIVE_PERCENT='sh_insttrans_o45'
        OVER_PLUS_FIFTY_PERCENT='sh_insttrans_o50'

    def filter_institutionaltransactions(self, institutionaltransactions: Institutionaltransactions):
        self.filters['Institutionaltransactions'] = institutionaltransactions

    class ShortFloat(str, Enum):
        """
        The amount of short-selling transactions of given stock.
        """
        LOW_LESSTHAN_FIVE_PERCENT='sh_short_low'
        HIGH_GREATERTHAN_TWENTY_PERCENT='sh_short_high'
        UNDER_FIVE_PERCENT='sh_short_u5'
        UNDER_TEN_PERCENT='sh_short_u10'
        UNDER_FIFTEEN_PERCENT='sh_short_u15'
        UNDER_TWENTY_PERCENT='sh_short_u20'
        UNDER_TWENTY_FIVE_PERCENT='sh_short_u25'
        UNDER_THIRTY_PERCENT='sh_short_u30'
        OVER_FIVE_PERCENT='sh_short_o5'
        OVER_TEN_PERCENT='sh_short_o10'
        OVER_FIFTEEN_PERCENT='sh_short_o15'
        OVER_TWENTY_PERCENT='sh_short_o20'
        OVER_TWENTY_FIVE_PERCENT='sh_short_o25'
        OVER_THIRTY_PERCENT='sh_short_o30'

    def filter_short_float(self, short_float: ShortFloat):
        self.filters['ShortFloat'] = short_float

    class AnalystRecom(str, Enum):
        """
        An outlook of a stock-market analyst on a stock.
        """
        STRONG_BUY_ONE='an_recom_strongbuy'
        BUY_OR_BETTER='an_recom_buybetter'
        BUY='an_recom_buy'
        HOLD_OR_BETTER='an_recom_holdbetter'
        HOLD='an_recom_hold'
        HOLD_OR_WORSE='an_recom_holdworse'
        SELL='an_recom_sell'
        SELL_OR_WORSE='an_recom_sellworse'
        STRONG_SELL_FIVE='an_recom_strongsell'

    def filter_analyst_recom(self, analyst_recom: AnalystRecom):
        self.filters['AnalystRecom'] = analyst_recom

    class OptionShort(str, Enum):
        """
        Stocks with options and/or available to sell short.
        """
        OPTIONABLE='sh_opt_option'
        SHORTABLE='sh_opt_short'
        NOT_OPTIONABLE='sh_opt_notoption'
        NOT_SHORTABLE='sh_opt_notshort'
        OPTIONABLE_AND_SHORTABLE='sh_opt_optionshort'
        OPTIONABLE_AND_NOT_SHORTABLE='sh_opt_optionnotshort'
        NOT_OPTIONABLE_AND_SHORTABLE='sh_opt_notoptionshort'
        NOT_OPTIONABLE_AND_NOT_SHORTABLE='sh_opt_notoptionnotshort'

    def filter_option_short(self, option_short: OptionShort):
        self.filters['OptionShort'] = option_short

    class EarningsDate(str, Enum):
        """
        Date when company reports earnings.
        """
        TODAY='earningsdate_today'
        TODAY_BEFORE_MARKET_OPEN='earningsdate_todaybefore'
        TODAY_AFTER_MARKET_CLOSE='earningsdate_todayafter'
        TOMORROW='earningsdate_tomorrow'
        TOMORROW_BEFORE_MARKET_OPEN='earningsdate_tomorrowbefore'
        TOMORROW_AFTER_MARKET_CLOSE='earningsdate_tomorrowafter'
        YESTERDAY='earningsdate_yesterday'
        YESTERDAY_BEFORE_MARKET_OPEN='earningsdate_yesterdaybefore'
        YESTERDAY_AFTER_MARKET_CLOSE='earningsdate_yesterdayafter'
        NEXT_FIVE_DAYS='earningsdate_nextdays5'
        PREVIOUS_FIVE_DAYS='earningsdate_prevdays5'
        THIS_WEEK='earningsdate_thisweek'
        NEXT_WEEK='earningsdate_nextweek'
        PREVIOUS_WEEK='earningsdate_prevweek'
        THIS_MONTH='earningsdate_thismonth'

    def filter_earnings_date(self, earnings_date: EarningsDate):
        self.filters['EarningsDate'] = earnings_date

    class Performance(str, Enum):
        """
        Rate of return for a given stock.
        """
        TODAY_UP='ta_perf_dup'
        TODAY_DOWN='ta_perf_ddown'
        TODAY_FIFTEEN_PERCENT='ta_perf_d15u'
        TODAY_TEN_PERCENT='ta_perf_d10u'
        TODAY_FIVE_PERCENT='ta_perf_d5u'
        TODAY_PLUS_FIVE_PERCENT='ta_perf_d5o'
        TODAY_PLUS_TEN_PERCENT='ta_perf_d10o'
        TODAY_PLUS_FIFTEEN_PERCENT='ta_perf_d15o'
        WEEK_THIRTY_PERCENT='ta_perf_1w30u'
        WEEK_TWENTY_PERCENT='ta_perf_1w20u'
        WEEK_TEN_PERCENT='ta_perf_1w10u'
        WEEK_DOWN='ta_perf_1wdown'
        WEEK_UP='ta_perf_1wup'
        WEEK_PLUS_TEN_PERCENT='ta_perf_1w10o'
        WEEK_PLUS_TWENTY_PERCENT='ta_perf_1w20o'
        WEEK_PLUS_THIRTY_PERCENT='ta_perf_1w30o'
        MONTH_FIFTY_PERCENT='ta_perf_4w50u'
        MONTH_THIRTY_PERCENT='ta_perf_4w30u'
        MONTH_TWENTY_PERCENT='ta_perf_4w20u'
        MONTH_TEN_PERCENT='ta_perf_4w10u'
        MONTH_DOWN='ta_perf_4wdown'
        MONTH_UP='ta_perf_4wup'
        MONTH_PLUS_TEN_PERCENT='ta_perf_4w10o'
        MONTH_PLUS_TWENTY_PERCENT='ta_perf_4w20o'
        MONTH_PLUS_THIRTY_PERCENT='ta_perf_4w30o'
        MONTH_PLUS_FIFTY_PERCENT='ta_perf_4w50o'
        QUARTER_FIFTY_PERCENT='ta_perf_13w50u'
        QUARTER_THIRTY_PERCENT='ta_perf_13w30u'
        QUARTER_TWENTY_PERCENT='ta_perf_13w20u'
        QUARTER_TEN_PERCENT='ta_perf_13w10u'
        QUARTER_DOWN='ta_perf_13wdown'
        QUARTER_UP='ta_perf_13wup'
        QUARTER_PLUS_TEN_PERCENT='ta_perf_13w10o'
        QUARTER_PLUS_TWENTY_PERCENT='ta_perf_13w20o'
        QUARTER_PLUS_THIRTY_PERCENT='ta_perf_13w30o'
        QUARTER_PLUS_FIFTY_PERCENT='ta_perf_13w50o'
        HALF_SEVENTY_FIVE_PERCENT='ta_perf_26w75u'
        HALF_FIFTY_PERCENT='ta_perf_26w50u'
        HALF_THIRTY_PERCENT='ta_perf_26w30u'
        HALF_TWENTY_PERCENT='ta_perf_26w20u'
        HALF_TEN_PERCENT='ta_perf_26w10u'
        HALF_DOWN='ta_perf_26wdown'
        HALF_UP='ta_perf_26wup'
        HALF_PLUS_TEN_PERCENT='ta_perf_26w10o'
        HALF_PLUS_TWENTY_PERCENT='ta_perf_26w20o'
        HALF_PLUS_THIRTY_PERCENT='ta_perf_26w30o'
        HALF_PLUS_FIFTY_PERCENT='ta_perf_26w50o'
        HALF_PLUS_ONE_HUNDRED_PERCENT='ta_perf_26w100o'
        YEAR_SEVENTY_FIVE_PERCENT='ta_perf_52w75u'
        YEAR_FIFTY_PERCENT='ta_perf_52w50u'
        YEAR_THIRTY_PERCENT='ta_perf_52w30u'
        YEAR_TWENTY_PERCENT='ta_perf_52w20u'
        YEAR_TEN_PERCENT='ta_perf_52w10u'
        YEAR_DOWN='ta_perf_52wdown'
        YEAR_UP='ta_perf_52wup'
        YEAR_PLUS_TEN_PERCENT='ta_perf_52w10o'
        YEAR_PLUS_TWENTY_PERCENT='ta_perf_52w20o'
        YEAR_PLUS_THIRTY_PERCENT='ta_perf_52w30o'
        YEAR_PLUS_FIFTY_PERCENT='ta_perf_52w50o'
        YEAR_PLUS_ONE_HUNDRED_PERCENT='ta_perf_52w100o'
        YEAR_PLUS_TWO_HUNDRED_PERCENT='ta_perf_52w200o'
        YEAR_PLUS_THREE_HUNDRED_PERCENT='ta_perf_52w300o'
        YEAR_PLUS_FIVE_HUNDRED_PERCENT='ta_perf_52w500o'
        YTD_SEVENTY_FIVE_PERCENT='ta_perf_ytd75u'
        YTD_FIFTY_PERCENT='ta_perf_ytd50u'
        YTD_THIRTY_PERCENT='ta_perf_ytd30u'
        YTD_TWENTY_PERCENT='ta_perf_ytd20u'
        YTD_TEN_PERCENT='ta_perf_ytd10u'
        YTD_FIVE_PERCENT='ta_perf_ytd5u'
        YTD_DOWN='ta_perf_ytddown'
        YTD_UP='ta_perf_ytdup'
        YTD_PLUS_FIVE_PERCENT='ta_perf_ytd5o'
        YTD_PLUS_TEN_PERCENT='ta_perf_ytd10o'
        YTD_PLUS_TWENTY_PERCENT='ta_perf_ytd20o'
        YTD_PLUS_THIRTY_PERCENT='ta_perf_ytd30o'
        YTD_PLUS_FIFTY_PERCENT='ta_perf_ytd50o'
        YTD_PLUS_ONE_HUNDRED_PERCENT='ta_perf_ytd100o'
        THREE_YEARS_NINETY_PERCENT='ta_perf_3y90u'
        THREE_YEARS_SEVENTY_FIVE_PERCENT='ta_perf_3y75u'
        THREE_YEARS_FIFTY_PERCENT='ta_perf_3y50u'
        THREE_YEARS_THIRTY_PERCENT='ta_perf_3y30u'
        THREE_YEARS_TWENTY_PERCENT='ta_perf_3y20u'
        THREE_YEARS_TEN_PERCENT='ta_perf_3y10u'
        THREE_YEARS_DOWN='ta_perf_3ydown'
        THREE_YEARS_UP='ta_perf_3yup'
        THREE_YEARS_PLUS_TEN_PERCENT='ta_perf_3y10o'
        THREE_YEARS_PLUS_TWENTY_PERCENT='ta_perf_3y20o'
        THREE_YEARS_PLUS_THIRTY_PERCENT='ta_perf_3y30o'
        THREE_YEARS_PLUS_FIFTY_PERCENT='ta_perf_3y50o'
        THREE_YEARS_PLUS_ONE_HUNDRED_PERCENT='ta_perf_3y100o'
        THREE_YEARS_PLUS_TWO_HUNDRED_PERCENT='ta_perf_3y200o'
        THREE_YEARS_PLUS_THREE_HUNDRED_PERCENT='ta_perf_3y300o'
        THREE_YEARS_PLUS_FIVE_HUNDRED_PERCENT='ta_perf_3y500o'
        THREE_YEARS_PLUS_ONE_THOUSAND_PERCENT='ta_perf_3y1000o'
        FIVE_YEARS_NINETY_PERCENT='ta_perf_5y90u'
        FIVE_YEARS_SEVENTY_FIVE_PERCENT='ta_perf_5y75u'
        FIVE_YEARS_FIFTY_PERCENT='ta_perf_5y50u'
        FIVE_YEARS_THIRTY_PERCENT='ta_perf_5y30u'
        FIVE_YEARS_TWENTY_PERCENT='ta_perf_5y20u'
        FIVE_YEARS_TEN_PERCENT='ta_perf_5y10u'
        FIVE_YEARS_DOWN='ta_perf_5ydown'
        FIVE_YEARS_UP='ta_perf_5yup'
        FIVE_YEARS_PLUS_TEN_PERCENT='ta_perf_5y10o'
        FIVE_YEARS_PLUS_TWENTY_PERCENT='ta_perf_5y20o'
        FIVE_YEARS_PLUS_THIRTY_PERCENT='ta_perf_5y30o'
        FIVE_YEARS_PLUS_FIFTY_PERCENT='ta_perf_5y50o'
        FIVE_YEARS_PLUS_ONE_HUNDRED_PERCENT='ta_perf_5y100o'
        FIVE_YEARS_PLUS_TWO_HUNDRED_PERCENT='ta_perf_5y200o'
        FIVE_YEARS_PLUS_THREE_HUNDRED_PERCENT='ta_perf_5y300o'
        FIVE_YEARS_PLUS_FIVE_HUNDRED_PERCENT='ta_perf_5y500o'
        FIVE_YEARS_PLUS_ONE_THOUSAND_PERCENT='ta_perf_5y1000o'
        TEN_YEARS_NINETY_PERCENT='ta_perf_10y90u'
        TEN_YEARS_SEVENTY_FIVE_PERCENT='ta_perf_10y75u'
        TEN_YEARS_FIFTY_PERCENT='ta_perf_10y50u'
        TEN_YEARS_THIRTY_PERCENT='ta_perf_10y30u'
        TEN_YEARS_TWENTY_PERCENT='ta_perf_10y20u'
        TEN_YEARS_TEN_PERCENT='ta_perf_10y10u'
        TEN_YEARS_DOWN='ta_perf_10ydown'
        TEN_YEARS_UP='ta_perf_10yup'
        TEN_YEARS_PLUS_TEN_PERCENT='ta_perf_10y10o'
        TEN_YEARS_PLUS_TWENTY_PERCENT='ta_perf_10y20o'
        TEN_YEARS_PLUS_THIRTY_PERCENT='ta_perf_10y30o'
        TEN_YEARS_PLUS_FIFTY_PERCENT='ta_perf_10y50o'
        TEN_YEARS_PLUS_ONE_HUNDRED_PERCENT='ta_perf_10y100o'
        TEN_YEARS_PLUS_TWO_HUNDRED_PERCENT='ta_perf_10y200o'
        TEN_YEARS_PLUS_THREE_HUNDRED_PERCENT='ta_perf_10y300o'
        TEN_YEARS_PLUS_FIVE_HUNDRED_PERCENT='ta_perf_10y500o'
        TEN_YEARS_PLUS_ONE_THOUSAND_PERCENT='ta_perf_10y1000o'

    def filter_performance(self, performance: Performance):
        self.filters['Performance'] = performance

    class PerformanceTwo(str, Enum):
        """
        Rate of return for a given stock.
        """
        TODAY_UP='ta_perf2_dup'
        TODAY_DOWN='ta_perf2_ddown'
        TODAY_FIFTEEN_PERCENT='ta_perf2_d15u'
        TODAY_TEN_PERCENT='ta_perf2_d10u'
        TODAY_FIVE_PERCENT='ta_perf2_d5u'
        TODAY_PLUS_FIVE_PERCENT='ta_perf2_d5o'
        TODAY_PLUS_TEN_PERCENT='ta_perf2_d10o'
        TODAY_PLUS_FIFTEEN_PERCENT='ta_perf2_d15o'
        WEEK_THIRTY_PERCENT='ta_perf2_1w30u'
        WEEK_TWENTY_PERCENT='ta_perf2_1w20u'
        WEEK_TEN_PERCENT='ta_perf2_1w10u'
        WEEK_DOWN='ta_perf2_1wdown'
        WEEK_UP='ta_perf2_1wup'
        WEEK_PLUS_TEN_PERCENT='ta_perf2_1w10o'
        WEEK_PLUS_TWENTY_PERCENT='ta_perf2_1w20o'
        WEEK_PLUS_THIRTY_PERCENT='ta_perf2_1w30o'
        MONTH_FIFTY_PERCENT='ta_perf2_4w50u'
        MONTH_THIRTY_PERCENT='ta_perf2_4w30u'
        MONTH_TWENTY_PERCENT='ta_perf2_4w20u'
        MONTH_TEN_PERCENT='ta_perf2_4w10u'
        MONTH_DOWN='ta_perf2_4wdown'
        MONTH_UP='ta_perf2_4wup'
        MONTH_PLUS_TEN_PERCENT='ta_perf2_4w10o'
        MONTH_PLUS_TWENTY_PERCENT='ta_perf2_4w20o'
        MONTH_PLUS_THIRTY_PERCENT='ta_perf2_4w30o'
        MONTH_PLUS_FIFTY_PERCENT='ta_perf2_4w50o'
        QUARTER_FIFTY_PERCENT='ta_perf2_13w50u'
        QUARTER_THIRTY_PERCENT='ta_perf2_13w30u'
        QUARTER_TWENTY_PERCENT='ta_perf2_13w20u'
        QUARTER_TEN_PERCENT='ta_perf2_13w10u'
        QUARTER_DOWN='ta_perf2_13wdown'
        QUARTER_UP='ta_perf2_13wup'
        QUARTER_PLUS_TEN_PERCENT='ta_perf2_13w10o'
        QUARTER_PLUS_TWENTY_PERCENT='ta_perf2_13w20o'
        QUARTER_PLUS_THIRTY_PERCENT='ta_perf2_13w30o'
        QUARTER_PLUS_FIFTY_PERCENT='ta_perf2_13w50o'
        HALF_SEVENTY_FIVE_PERCENT='ta_perf2_26w75u'
        HALF_FIFTY_PERCENT='ta_perf2_26w50u'
        HALF_THIRTY_PERCENT='ta_perf2_26w30u'
        HALF_TWENTY_PERCENT='ta_perf2_26w20u'
        HALF_TEN_PERCENT='ta_perf2_26w10u'
        HALF_DOWN='ta_perf2_26wdown'
        HALF_UP='ta_perf2_26wup'
        HALF_PLUS_TEN_PERCENT='ta_perf2_26w10o'
        HALF_PLUS_TWENTY_PERCENT='ta_perf2_26w20o'
        HALF_PLUS_THIRTY_PERCENT='ta_perf2_26w30o'
        HALF_PLUS_FIFTY_PERCENT='ta_perf2_26w50o'
        HALF_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_26w100o'
        YEAR_SEVENTY_FIVE_PERCENT='ta_perf2_52w75u'
        YEAR_FIFTY_PERCENT='ta_perf2_52w50u'
        YEAR_THIRTY_PERCENT='ta_perf2_52w30u'
        YEAR_TWENTY_PERCENT='ta_perf2_52w20u'
        YEAR_TEN_PERCENT='ta_perf2_52w10u'
        YEAR_DOWN='ta_perf2_52wdown'
        YEAR_UP='ta_perf2_52wup'
        YEAR_PLUS_TEN_PERCENT='ta_perf2_52w10o'
        YEAR_PLUS_TWENTY_PERCENT='ta_perf2_52w20o'
        YEAR_PLUS_THIRTY_PERCENT='ta_perf2_52w30o'
        YEAR_PLUS_FIFTY_PERCENT='ta_perf2_52w50o'
        YEAR_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_52w100o'
        YEAR_PLUS_TWO_HUNDRED_PERCENT='ta_perf2_52w200o'
        YEAR_PLUS_THREE_HUNDRED_PERCENT='ta_perf2_52w300o'
        YEAR_PLUS_FIVE_HUNDRED_PERCENT='ta_perf2_52w500o'
        YTD_SEVENTY_FIVE_PERCENT='ta_perf2_ytd75u'
        YTD_FIFTY_PERCENT='ta_perf2_ytd50u'
        YTD_THIRTY_PERCENT='ta_perf2_ytd30u'
        YTD_TWENTY_PERCENT='ta_perf2_ytd20u'
        YTD_TEN_PERCENT='ta_perf2_ytd10u'
        YTD_FIVE_PERCENT='ta_perf2_ytd5u'
        YTD_DOWN='ta_perf2_ytddown'
        YTD_UP='ta_perf2_ytdup'
        YTD_PLUS_FIVE_PERCENT='ta_perf2_ytd5o'
        YTD_PLUS_TEN_PERCENT='ta_perf2_ytd10o'
        YTD_PLUS_TWENTY_PERCENT='ta_perf2_ytd20o'
        YTD_PLUS_THIRTY_PERCENT='ta_perf2_ytd30o'
        YTD_PLUS_FIFTY_PERCENT='ta_perf2_ytd50o'
        YTD_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_ytd100o'
        THREE_YEAR_NINETY_PERCENT='ta_perf2_3y90u'
        THREE_YEAR_SEVENTY_FIVE_PERCENT='ta_perf2_3y75u'
        THREE_YEAR_FIFTY_PERCENT='ta_perf2_3y50u'
        THREE_YEAR_THIRTY_PERCENT='ta_perf2_3y30u'
        THREE_YEAR_TWENTY_PERCENT='ta_perf2_3y20u'
        THREE_YEAR_TEN_PERCENT='ta_perf2_3y10u'
        THREE_YEAR_DOWN='ta_perf2_3ydown'
        THREE_YEAR_UP='ta_perf2_3yup'
        THREE_YEAR_PLUS_TEN_PERCENT='ta_perf2_3y10o'
        THREE_YEAR_PLUS_TWENTY_PERCENT='ta_perf2_3y20o'
        THREE_YEAR_PLUS_THIRTY_PERCENT='ta_perf2_3y30o'
        THREE_YEAR_PLUS_FIFTY_PERCENT='ta_perf2_3y50o'
        THREE_YEAR_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_3y100o'
        THREE_YEAR_PLUS_TWO_HUNDRED_PERCENT='ta_perf2_3y200o'
        THREE_YEAR_PLUS_THREE_HUNDRED_PERCENT='ta_perf2_3y300o'
        THREE_YEAR_PLUS_FIVE_HUNDRED_PERCENT='ta_perf2_3y500o'
        THREE_YEAR_PLUS_ONE_THOUSAND_PERCENT='ta_perf2_3y1000o'
        FIVE_YEAR_NINETY_PERCENT='ta_perf2_5y90u'
        FIVE_YEAR_SEVENTY_FIVE_PERCENT='ta_perf2_5y75u'
        FIVE_YEAR_FIFTY_PERCENT='ta_perf2_5y50u'
        FIVE_YEAR_THIRTY_PERCENT='ta_perf2_5y30u'
        FIVE_YEAR_TWENTY_PERCENT='ta_perf2_5y20u'
        FIVE_YEAR_TEN_PERCENT='ta_perf2_5y10u'
        FIVE_YEAR_DOWN='ta_perf2_5ydown'
        FIVE_YEAR_UP='ta_perf2_5yup'
        FIVE_YEAR_PLUS_TEN_PERCENT='ta_perf2_5y10o'
        FIVE_YEAR_PLUS_TWENTY_PERCENT='ta_perf2_5y20o'
        FIVE_YEAR_PLUS_THIRTY_PERCENT='ta_perf2_5y30o'
        FIVE_YEAR_PLUS_FIFTY_PERCENT='ta_perf2_5y50o'
        FIVE_YEAR_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_5y100o'
        FIVE_YEAR_PLUS_TWO_HUNDRED_PERCENT='ta_perf2_5y200o'
        FIVE_YEAR_PLUS_THREE_HUNDRED_PERCENT='ta_perf2_5y300o'
        FIVE_YEAR_PLUS_FIVE_HUNDRED_PERCENT='ta_perf2_5y500o'
        FIVE_YEAR_PLUS_ONE_THOUSAND_PERCENT='ta_perf2_5y1000o'
        TEN_YEAR_NINETY_PERCENT='ta_perf2_10y90u'
        TEN_YEAR_SEVENTY_FIVE_PERCENT='ta_perf2_10y75u'
        TEN_YEAR_FIFTY_PERCENT='ta_perf2_10y50u'
        TEN_YEAR_THIRTY_PERCENT='ta_perf2_10y30u'
        TEN_YEAR_TWENTY_PERCENT='ta_perf2_10y20u'
        TEN_YEAR_TEN_PERCENT='ta_perf2_10y10u'
        TEN_YEAR_DOWN='ta_perf2_10ydown'
        TEN_YEAR_UP='ta_perf2_10yup'
        TEN_YEAR_PLUS_TEN_PERCENT='ta_perf2_10y10o'
        TEN_YEAR_PLUS_TWENTY_PERCENT='ta_perf2_10y20o'
        TEN_YEAR_PLUS_THIRTY_PERCENT='ta_perf2_10y30o'
        TEN_YEAR_PLUS_FIFTY_PERCENT='ta_perf2_10y50o'
        TEN_YEAR_PLUS_ONE_HUNDRED_PERCENT='ta_perf2_10y100o'
        TEN_YEAR_PLUS_TWO_HUNDRED_PERCENT='ta_perf2_10y200o'
        TEN_YEAR_PLUS_THREE_HUNDRED_PERCENT='ta_perf2_10y300o'
        TEN_YEAR_PLUS_FIVE_HUNDRED_PERCENT='ta_perf2_10y500o'
        TEN_YEAR_PLUS_ONE_THOUSAND_PERCENT='ta_perf2_10y1000o'

    def filter_performance_two(self, performance_two: PerformanceTwo):
        self.filters['PerformanceTwo'] = performance_two

    class Volatility(str, Enum):
        """
        A statistical measure of the dispersion of returns for a given stock. Represents average daily high/low trading range.
        """
        WEEK_OVER_TWO_PERCENT='ta_volatility_wo2'
        WEEK_OVER_THREE_PERCENT='ta_volatility_wo3'
        WEEK_OVER_FOUR_PERCENT='ta_volatility_wo4'
        WEEK_OVER_FIVE_PERCENT='ta_volatility_wo5'
        WEEK_OVER_SIX_PERCENT='ta_volatility_wo6'
        WEEK_OVER_SEVEN_PERCENT='ta_volatility_wo7'
        WEEK_OVER_EIGHT_PERCENT='ta_volatility_wo8'
        WEEK_OVER_NINE_PERCENT='ta_volatility_wo9'
        WEEK_OVER_TEN_PERCENT='ta_volatility_wo10'
        WEEK_OVER_TWELVE_PERCENT='ta_volatility_wo12'
        WEEK_OVER_FIFTEEN_PERCENT='ta_volatility_wo15'
        MONTH_OVER_TWO_PERCENT='ta_volatility_mo2'
        MONTH_OVER_THREE_PERCENT='ta_volatility_mo3'
        MONTH_OVER_FOUR_PERCENT='ta_volatility_mo4'
        MONTH_OVER_FIVE_PERCENT='ta_volatility_mo5'
        MONTH_OVER_SIX_PERCENT='ta_volatility_mo6'
        MONTH_OVER_SEVEN_PERCENT='ta_volatility_mo7'
        MONTH_OVER_EIGHT_PERCENT='ta_volatility_mo8'
        MONTH_OVER_NINE_PERCENT='ta_volatility_mo9'
        MONTH_OVER_TEN_PERCENT='ta_volatility_mo10'
        MONTH_OVER_TWELVE_PERCENT='ta_volatility_mo12'
        MONTH_OVER_FIFTEEN_PERCENT='ta_volatility_mo15'

    def filter_volatility(self, volatility: Volatility):
        self.filters['Volatility'] = volatility

    class RsiFourteen(str, Enum):
        """
        The Relative Strength Index (RSI) is a technical analysis oscillator showing price strength by comparing upward and downward close-to-close movements.
        """
        OVERBOUGHT_NINETY='ta_rsi_ob90'
        OVERBOUGHT_EIGHTY='ta_rsi_ob80'
        OVERBOUGHT_SEVENTY='ta_rsi_ob70'
        OVERBOUGHT_SIXTY='ta_rsi_ob60'
        OVERSOLD_FORTY='ta_rsi_os40'
        OVERSOLD_THIRTY='ta_rsi_os30'
        OVERSOLD_TWENTY='ta_rsi_os20'
        OVERSOLD_TEN='ta_rsi_os10'
        NOT_OVERBOUGHT_LESSTHAN_SIXTY='ta_rsi_nob60'
        NOT_OVERBOUGHT_LESSTHAN_FIFTY='ta_rsi_nob50'
        NOT_OVERSOLD_GREATERTHAN_FIFTY='ta_rsi_nos50'
        NOT_OVERSOLD_GREATERTHAN_FORTY='ta_rsi_nos40'

    def filter_rsi_fourteen(self, rsi_fourteen: RsiFourteen):
        self.filters['RsiFourteen'] = rsi_fourteen

    class Gap(str, Enum):
        """
        The difference between yesterday's closing price and today's opening price.
        """
        UP='ta_gap_u'
        UP_ZERO_PERCENT='ta_gap_u0'
        UP_ONE_PERCENT='ta_gap_u1'
        UP_TWO_PERCENT='ta_gap_u2'
        UP_THREE_PERCENT='ta_gap_u3'
        UP_FOUR_PERCENT='ta_gap_u4'
        UP_FIVE_PERCENT='ta_gap_u5'
        UP_SIX_PERCENT='ta_gap_u6'
        UP_SEVEN_PERCENT='ta_gap_u7'
        UP_EIGHT_PERCENT='ta_gap_u8'
        UP_NINE_PERCENT='ta_gap_u9'
        UP_TEN_PERCENT='ta_gap_u10'
        UP_FIFTEEN_PERCENT='ta_gap_u15'
        UP_TWENTY_PERCENT='ta_gap_u20'
        DOWN='ta_gap_d'
        DOWN_ZERO_PERCENT='ta_gap_d0'
        DOWN_ONE_PERCENT='ta_gap_d1'
        DOWN_TWO_PERCENT='ta_gap_d2'
        DOWN_THREE_PERCENT='ta_gap_d3'
        DOWN_FOUR_PERCENT='ta_gap_d4'
        DOWN_FIVE_PERCENT='ta_gap_d5'
        DOWN_SIX_PERCENT='ta_gap_d6'
        DOWN_SEVEN_PERCENT='ta_gap_d7'
        DOWN_EIGHT_PERCENT='ta_gap_d8'
        DOWN_NINE_PERCENT='ta_gap_d9'
        DOWN_TEN_PERCENT='ta_gap_d10'
        DOWN_FIFTEEN_PERCENT='ta_gap_d15'
        DOWN_TWENTY_PERCENT='ta_gap_d20'

    def filter_gap(self, gap: Gap):
        self.filters['Gap'] = gap

    class SimpleMovingAverage20Day(str, Enum):
        """
        20-Day simple moving average of closing price is the mean of the previous 20 days' closing prices.
        """
        PRICE_BELOW_SMA_TWENTY='ta_sma20_pb'
        PRICE_TEN_PERCENT_BELOW_SMA_TWENTY='ta_sma20_pb10'
        PRICE_TWENTY_PERCENT_BELOW_SMA_TWENTY='ta_sma20_pb20'
        PRICE_THIRTY_PERCENT_BELOW_SMA_TWENTY='ta_sma20_pb30'
        PRICE_FORTY_PERCENT_BELOW_SMA_TWENTY='ta_sma20_pb40'
        PRICE_FIFTY_PERCENT_BELOW_SMA_TWENTY='ta_sma20_pb50'
        PRICE_ABOVE_SMA_TWENTY='ta_sma20_pa'
        PRICE_TEN_PERCENT_ABOVE_SMA_TWENTY='ta_sma20_pa10'
        PRICE_TWENTY_PERCENT_ABOVE_SMA_TWENTY='ta_sma20_pa20'
        PRICE_THIRTY_PERCENT_ABOVE_SMA_TWENTY='ta_sma20_pa30'
        PRICE_FORTY_PERCENT_ABOVE_SMA_TWENTY='ta_sma20_pa40'
        PRICE_FIFTY_PERCENT_ABOVE_SMA_TWENTY='ta_sma20_pa50'
        PRICE_CROSSED_SMA_TWENTY='ta_sma20_pc'
        PRICE_CROSSED_SMA_TWENTY_ABOVE='ta_sma20_pca'
        PRICE_CROSSED_SMA_TWENTY_BELOW='ta_sma20_pcb'
        SMA_TWENTY_CROSSED_SMA_FIFTY='ta_sma20_cross50'
        SMA_TWENTY_CROSSED_SMA_FIFTY_ABOVE='ta_sma20_cross50a'
        SMA_TWENTY_CROSSED_SMA_FIFTY_BELOW='ta_sma20_cross50b'
        SMA_TWENTY_CROSSED_SMA_TWO_HUNDRED='ta_sma20_cross200'
        SMA_TWENTY_CROSSED_SMA_TWO_HUNDRED_ABOVE='ta_sma20_cross200a'
        SMA_TWENTY_CROSSED_SMA_TWO_HUNDRED_BELOW='ta_sma20_cross200b'
        SMA_TWENTY_ABOVE_SMA_FIFTY='ta_sma20_sa50'
        SMA_TWENTY_BELOW_SMA_FIFTY='ta_sma20_sb50'
        SMA_TWENTY_ABOVE_SMA_TWO_HUNDRED='ta_sma20_sa200'
        SMA_TWENTY_BELOW_SMA_TWO_HUNDRED='ta_sma20_sb200'

    def filter_simple_moving_average_20_day(self, simple_moving_average_20_day: SimpleMovingAverage20Day):
        self.filters['SimpleMovingAverage20Day'] = simple_moving_average_20_day

    class SimpleMovingAverage50Day(str, Enum):
        """
        50-Day simple moving average of closing price is the mean of the previous 50 days' closing prices.
        """
        PRICE_BELOW_SMA_FIFTY='ta_sma50_pb'
        PRICE_TEN_PERCENT_BELOW_SMA_FIFTY='ta_sma50_pb10'
        PRICE_TWENTY_PERCENT_BELOW_SMA_FIFTY='ta_sma50_pb20'
        PRICE_THIRTY_PERCENT_BELOW_SMA_FIFTY='ta_sma50_pb30'
        PRICE_FORTY_PERCENT_BELOW_SMA_FIFTY='ta_sma50_pb40'
        PRICE_FIFTY_PERCENT_BELOW_SMA_FIFTY='ta_sma50_pb50'
        PRICE_ABOVE_SMA_FIFTY='ta_sma50_pa'
        PRICE_TEN_PERCENT_ABOVE_SMA_FIFTY='ta_sma50_pa10'
        PRICE_TWENTY_PERCENT_ABOVE_SMA_FIFTY='ta_sma50_pa20'
        PRICE_THIRTY_PERCENT_ABOVE_SMA_FIFTY='ta_sma50_pa30'
        PRICE_FORTY_PERCENT_ABOVE_SMA_FIFTY='ta_sma50_pa40'
        PRICE_FIFTY_PERCENT_ABOVE_SMA_FIFTY='ta_sma50_pa50'
        PRICE_CROSSED_SMA_FIFTY='ta_sma50_pc'
        PRICE_CROSSED_SMA_FIFTY_ABOVE='ta_sma50_pca'
        PRICE_CROSSED_SMA_FIFTY_BELOW='ta_sma50_pcb'
        SMA_FIFTY_CROSSED_SMA_TWENTY='ta_sma50_cross20'
        SMA_FIFTY_CROSSED_SMA_TWENTY_ABOVE='ta_sma50_cross20a'
        SMA_FIFTY_CROSSED_SMA_TWENTY_BELOW='ta_sma50_cross20b'
        SMA_FIFTY_CROSSED_SMA_TWO_HUNDRED='ta_sma50_cross200'
        SMA_FIFTY_CROSSED_SMA_TWO_HUNDRED_ABOVE='ta_sma50_cross200a'
        SMA_FIFTY_CROSSED_SMA_TWO_HUNDRED_BELOW='ta_sma50_cross200b'
        SMA_FIFTY_ABOVE_SMA_TWENTY='ta_sma50_sa20'
        SMA_FIFTY_BELOW_SMA_TWENTY='ta_sma50_sb20'
        SMA_FIFTY_ABOVE_SMA_TWO_HUNDRED='ta_sma50_sa200'
        SMA_FIFTY_BELOW_SMA_TWO_HUNDRED='ta_sma50_sb200'

    def filter_simple_moving_average_50_day(self, simple_moving_average_50_day: SimpleMovingAverage50Day):
        self.filters['SimpleMovingAverage50Day'] = simple_moving_average_50_day

    class SimpleMovingAverage200Day(str, Enum):
        """
        200-Day simple moving average of closing price is the mean of the previous 200 days' closing prices.
        """
        PRICE_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb'
        PRICE_TEN_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb10'
        PRICE_TWENTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb20'
        PRICE_THIRTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb30'
        PRICE_FORTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb40'
        PRICE_FIFTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb50'
        PRICE_SIXTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb60'
        PRICE_SEVENTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb70'
        PRICE_EIGHTY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb80'
        PRICE_NINETY_PERCENT_BELOW_SMA_TWO_HUNDRED='ta_sma200_pb90'
        PRICE_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa'
        PRICE_TEN_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa10'
        PRICE_TWENTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa20'
        PRICE_THIRTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa30'
        PRICE_FORTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa40'
        PRICE_FIFTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa50'
        PRICE_SIXTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa60'
        PRICE_SEVENTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa70'
        PRICE_EIGHTY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa80'
        PRICE_NINETY_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa90'
        PRICE_ONE_HUNDRED_PERCENT_ABOVE_SMA_TWO_HUNDRED='ta_sma200_pa100'
        PRICE_CROSSED_SMA_TWO_HUNDRED='ta_sma200_pc'
        PRICE_CROSSED_SMA_TWO_HUNDRED_ABOVE='ta_sma200_pca'
        PRICE_CROSSED_SMA_TWO_HUNDRED_BELOW='ta_sma200_pcb'
        SMA_TWO_HUNDRED_CROSSED_SMA_TWENTY='ta_sma200_cross20'
        SMA_TWO_HUNDRED_CROSSED_SMA_TWENTY_ABOVE='ta_sma200_cross20a'
        SMA_TWO_HUNDRED_CROSSED_SMA_TWENTY_BELOW='ta_sma200_cross20b'
        SMA_TWO_HUNDRED_CROSSED_SMA_FIFTY='ta_sma200_cross50'
        SMA_TWO_HUNDRED_CROSSED_SMA_FIFTY_ABOVE='ta_sma200_cross50a'
        SMA_TWO_HUNDRED_CROSSED_SMA_FIFTY_BELOW='ta_sma200_cross50b'
        SMA_TWO_HUNDRED_ABOVE_SMA_TWENTY='ta_sma200_sa20'
        SMA_TWO_HUNDRED_BELOW_SMA_TWENTY='ta_sma200_sb20'
        SMA_TWO_HUNDRED_ABOVE_SMA_FIFTY='ta_sma200_sa50'
        SMA_TWO_HUNDRED_BELOW_SMA_FIFTY='ta_sma200_sb50'

    def filter_simple_moving_average_200_day(self, simple_moving_average_200_day: SimpleMovingAverage200Day):
        self.filters['SimpleMovingAverage200Day'] = simple_moving_average_200_day

    class Change(str, Enum):
        """
        The difference between previous's close price and today's last price.
        """
        UP='ta_change_u'
        UP_ONE_PERCENT='ta_change_u1'
        UP_TWO_PERCENT='ta_change_u2'
        UP_THREE_PERCENT='ta_change_u3'
        UP_FOUR_PERCENT='ta_change_u4'
        UP_FIVE_PERCENT='ta_change_u5'
        UP_SIX_PERCENT='ta_change_u6'
        UP_SEVEN_PERCENT='ta_change_u7'
        UP_EIGHT_PERCENT='ta_change_u8'
        UP_NINE_PERCENT='ta_change_u9'
        UP_TEN_PERCENT='ta_change_u10'
        UP_FIFTEEN_PERCENT='ta_change_u15'
        UP_TWENTY_PERCENT='ta_change_u20'
        DOWN='ta_change_d'
        DOWN_ONE_PERCENT='ta_change_d1'
        DOWN_TWO_PERCENT='ta_change_d2'
        DOWN_THREE_PERCENT='ta_change_d3'
        DOWN_FOUR_PERCENT='ta_change_d4'
        DOWN_FIVE_PERCENT='ta_change_d5'
        DOWN_SIX_PERCENT='ta_change_d6'
        DOWN_SEVEN_PERCENT='ta_change_d7'
        DOWN_EIGHT_PERCENT='ta_change_d8'
        DOWN_NINE_PERCENT='ta_change_d9'
        DOWN_TEN_PERCENT='ta_change_d10'
        DOWN_FIFTEEN_PERCENT='ta_change_d15'
        DOWN_TWENTY_PERCENT='ta_change_d20'

    def filter_change(self, change: Change):
        self.filters['Change'] = change

    class ChangeFromOpen(str, Enum):
        """
        The difference between today's open price and today's last price.
        """
        UP='ta_changeopen_u'
        UP_ONE_PERCENT='ta_changeopen_u1'
        UP_TWO_PERCENT='ta_changeopen_u2'
        UP_THREE_PERCENT='ta_changeopen_u3'
        UP_FOUR_PERCENT='ta_changeopen_u4'
        UP_FIVE_PERCENT='ta_changeopen_u5'
        UP_SIX_PERCENT='ta_changeopen_u6'
        UP_SEVEN_PERCENT='ta_changeopen_u7'
        UP_EIGHT_PERCENT='ta_changeopen_u8'
        UP_NINE_PERCENT='ta_changeopen_u9'
        UP_TEN_PERCENT='ta_changeopen_u10'
        UP_FIFTEEN_PERCENT='ta_changeopen_u15'
        UP_TWENTY_PERCENT='ta_changeopen_u20'
        DOWN='ta_changeopen_d'
        DOWN_ONE_PERCENT='ta_changeopen_d1'
        DOWN_TWO_PERCENT='ta_changeopen_d2'
        DOWN_THREE_PERCENT='ta_changeopen_d3'
        DOWN_FOUR_PERCENT='ta_changeopen_d4'
        DOWN_FIVE_PERCENT='ta_changeopen_d5'
        DOWN_SIX_PERCENT='ta_changeopen_d6'
        DOWN_SEVEN_PERCENT='ta_changeopen_d7'
        DOWN_EIGHT_PERCENT='ta_changeopen_d8'
        DOWN_NINE_PERCENT='ta_changeopen_d9'
        DOWN_TEN_PERCENT='ta_changeopen_d10'
        DOWN_FIFTEEN_PERCENT='ta_changeopen_d15'
        DOWN_TWENTY_PERCENT='ta_changeopen_d20'

    def filter_change_from_open(self, change_from_open: ChangeFromOpen):
        self.filters['ChangeFromOpen'] = change_from_open

    class HighLow20Day(str, Enum):
        """
        Maximum/minimum of previous 20 days' highs/lows.
        """
        NEW_HIGH='ta_highlow20d_nh'
        NEW_LOW='ta_highlow20d_nl'
        FIVE_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b5h'
        TEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b10h'
        FIFTEEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b15h'
        TWENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b20h'
        THIRTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b30h'
        FORTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b40h'
        FIFTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow20d_b50h'
        ZERO_THREE_PERCENT_BELOW_HIGH='ta_highlow20d_b0to3h'
        ZERO_FIVE_PERCENT_BELOW_HIGH='ta_highlow20d_b0to5h'
        ZERO_TEN_PERCENT_BELOW_HIGH='ta_highlow20d_b0to10h'
        FIVE_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a5h'
        TEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a10h'
        FIFTEEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a15h'
        TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a20h'
        THIRTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a30h'
        FORTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a40h'
        FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow20d_a50h'
        ZERO_THREE_PERCENT_ABOVE_LOW='ta_highlow20d_a0to3h'
        ZERO_FIVE_PERCENT_ABOVE_LOW='ta_highlow20d_a0to5h'
        ZERO_TEN_PERCENT_ABOVE_LOW='ta_highlow20d_a0to10h'

    def filter_high_low_20_day(self, high_low_20_day: HighLow20Day):
        self.filters['HighLow20Day'] = high_low_20_day

    class HighLow50Day(str, Enum):
        """
        Maximum/minimum of previous 50 days' highs/lows.
        """
        NEW_HIGH='ta_highlow50d_nh'
        NEW_LOW='ta_highlow50d_nl'
        FIVE_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b5h'
        TEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b10h'
        FIFTEEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b15h'
        TWENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b20h'
        THIRTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b30h'
        FORTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b40h'
        FIFTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow50d_b50h'
        ZERO_THREE_PERCENT_BELOW_HIGH='ta_highlow50d_b0to3h'
        ZERO_FIVE_PERCENT_BELOW_HIGH='ta_highlow50d_b0to5h'
        ZERO_TEN_PERCENT_BELOW_HIGH='ta_highlow50d_b0to10h'
        FIVE_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a5h'
        TEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a10h'
        FIFTEEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a15h'
        TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a20h'
        THIRTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a30h'
        FORTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a40h'
        FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow50d_a50h'
        ZERO_THREE_PERCENT_ABOVE_LOW='ta_highlow50d_a0to3h'
        ZERO_FIVE_PERCENT_ABOVE_LOW='ta_highlow50d_a0to5h'
        ZERO_TEN_PERCENT_ABOVE_LOW='ta_highlow50d_a0to10h'

    def filter_high_low_50_day(self, high_low_50_day: HighLow50Day):
        self.filters['HighLow50Day'] = high_low_50_day

    class FiftyTwoWeekHighLow(str, Enum):
        """
        Maximum/minimum of previous 52 weeks' highs/lows.
        """
        NEW_HIGH='ta_highlow52w_nh'
        NEW_LOW='ta_highlow52w_nl'
        FIVE_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b5h'
        TEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b10h'
        FIFTEEN_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b15h'
        TWENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b20h'
        THIRTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b30h'
        FORTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b40h'
        FIFTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b50h'
        SIXTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b60h'
        SEVENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b70h'
        EIGHTY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b80h'
        NINETY_PERCENT_OR_MORE_BELOW_HIGH='ta_highlow52w_b90h'
        ZERO_THREE_PERCENT_BELOW_HIGH='ta_highlow52w_b0to3h'
        ZERO_FIVE_PERCENT_BELOW_HIGH='ta_highlow52w_b0to5h'
        ZERO_TEN_PERCENT_BELOW_HIGH='ta_highlow52w_b0to10h'
        FIVE_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a5h'
        TEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a10h'
        FIFTEEN_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a15h'
        TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a20h'
        THIRTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a30h'
        FORTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a40h'
        FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a50h'
        SIXTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a60h'
        SEVENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a70h'
        EIGHTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a80h'
        NINETY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a90h'
        ONE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a100h'
        ONE_HUNDRED_AND_TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a120h'
        ONE_HUNDRED_AND_FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a150h'
        TWO_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a200h'
        THREE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a300h'
        FIVE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_highlow52w_a500h'
        ZERO_THREE_PERCENT_ABOVE_LOW='ta_highlow52w_a0to3h'
        ZERO_FIVE_PERCENT_ABOVE_LOW='ta_highlow52w_a0to5h'
        ZERO_TEN_PERCENT_ABOVE_LOW='ta_highlow52w_a0to10h'

    def filter_fifty_two_week_high_low(self, fifty_two_week_high_low: FiftyTwoWeekHighLow):
        self.filters['FiftyTwoWeekHighLow'] = fifty_two_week_high_low

    class AllTimeHighLow(str, Enum):
        """
        Maximum/minimum of all-time highs/lows.
        """
        NEW_HIGH='ta_alltime_nh'
        NEW_LOW='ta_alltime_nl'
        FIVE_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b5h'
        TEN_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b10h'
        FIFTEEN_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b15h'
        TWENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b20h'
        THIRTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b30h'
        FORTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b40h'
        FIFTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b50h'
        SIXTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b60h'
        SEVENTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b70h'
        EIGHTY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b80h'
        NINETY_PERCENT_OR_MORE_BELOW_HIGH='ta_alltime_b90h'
        ZERO_THREE_PERCENT_BELOW_HIGH='ta_alltime_b0to3h'
        ZERO_FIVE_PERCENT_BELOW_HIGH='ta_alltime_b0to5h'
        ZERO_TEN_PERCENT_BELOW_HIGH='ta_alltime_b0to10h'
        FIVE_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a5h'
        TEN_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a10h'
        FIFTEEN_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a15h'
        TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a20h'
        THIRTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a30h'
        FORTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a40h'
        FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a50h'
        SIXTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a60h'
        SEVENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a70h'
        EIGHTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a80h'
        NINETY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a90h'
        ONE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a100h'
        ONE_HUNDRED_AND_TWENTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a120h'
        ONE_HUNDRED_AND_FIFTY_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a150h'
        TWO_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a200h'
        THREE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a300h'
        FIVE_HUNDRED_PERCENT_OR_MORE_ABOVE_LOW='ta_alltime_a500h'
        ZERO_THREE_PERCENT_ABOVE_LOW='ta_alltime_a0to3h'
        ZERO_FIVE_PERCENT_ABOVE_LOW='ta_alltime_a0to5h'
        ZERO_TEN_PERCENT_ABOVE_LOW='ta_alltime_a0to10h'

    def filter_all_time_high_low(self, all_time_high_low: AllTimeHighLow):
        self.filters['AllTimeHighLow'] = all_time_high_low

    class Pattern(str, Enum):
        """
        A chart pattern is a distinct formation on a stock chart that creates a trading signal, or a sign of future price movements. Chartists use these patterns to identify current trends and trend reversals and to trigger buy and sell signals.
        """
        HORIZONTAL_S_R='ta_pattern_horizontal'
        HORIZONTAL_S_R_STRONG='ta_pattern_horizontal2'
        TL_RESISTANCE='ta_pattern_tlresistance'
        TL_RESISTANCE_STRONG='ta_pattern_tlresistance2'
        TL_SUPPORT='ta_pattern_tlsupport'
        TL_SUPPORT_STRONG='ta_pattern_tlsupport2'
        WEDGE_UP='ta_pattern_wedgeup'
        WEDGE_UP_STRONG='ta_pattern_wedgeup2'
        WEDGE_DOWN='ta_pattern_wedgedown'
        WEDGE_DOWN_STRONG='ta_pattern_wedgedown2'
        TRIANGLE_ASCENDING='ta_pattern_wedgeresistance'
        TRIANGLE_ASCENDING_STRONG='ta_pattern_wedgeresistance2'
        TRIANGLE_DESCENDING='ta_pattern_wedgesupport'
        TRIANGLE_DESCENDING_STRONG='ta_pattern_wedgesupport2'
        WEDGE='ta_pattern_wedge'
        WEDGE_STRONG='ta_pattern_wedge2'
        CHANNEL_UP='ta_pattern_channelup'
        CHANNEL_UP_STRONG='ta_pattern_channelup2'
        CHANNEL_DOWN='ta_pattern_channeldown'
        CHANNEL_DOWN_STRONG='ta_pattern_channeldown2'
        CHANNEL='ta_pattern_channel'
        CHANNEL_STRONG='ta_pattern_channel2'
        DOUBLE_TOP='ta_pattern_doubletop'
        DOUBLE_BOTTOM='ta_pattern_doublebottom'
        MULTIPLE_TOP='ta_pattern_multipletop'
        MULTIPLE_BOTTOM='ta_pattern_multiplebottom'
        HEAD_AND_SHOULDERS='ta_pattern_headandshoulders'
        HEAD_AND_SHOULDERS_INVERSE='ta_pattern_headandshouldersinv'

    def filter_pattern(self, pattern: Pattern):
        self.filters['Pattern'] = pattern

    class Candlestick(str, Enum):
        """
        Candlesticks are usually composed of the body (black or white), an upper and a lower shadow (wick). The wick illustrates the highest and lowest traded prices of a stock during the time interval represented. The body illustrates the opening and closing trades.
        """
        LONG_LOWER_SHADOW='ta_candlestick_lls'
        LONG_UPPER_SHADOW='ta_candlestick_lus'
        HAMMER='ta_candlestick_h'
        INVERTED_HAMMER='ta_candlestick_ih'
        SPINNING_TOP_WHITE='ta_candlestick_stw'
        SPINNING_TOP_BLACK='ta_candlestick_stb'
        DOJI='ta_candlestick_d'
        DRAGONFLY_DOJI='ta_candlestick_dd'
        GRAVESTONE_DOJI='ta_candlestick_gd'
        MARUBOZU_WHITE='ta_candlestick_mw'
        MARUBOZU_BLACK='ta_candlestick_mb'

    def filter_candlestick(self, candlestick: Candlestick):
        self.filters['Candlestick'] = candlestick

    class Beta(str, Enum):
        """
        A measure of a stock’s price volatility relative to the market. An asset with a beta of 0 means that its price is not at all correlated with the market. A positive beta means that the asset generally follows the market. A negative beta shows that the asset inversely follows the market, decreases in value if the market goes up.
        """
        UNDER_ZERO='ta_beta_u0'
        UNDER_ZERO_FIVE='ta_beta_u0.5'
        UNDER_ONE='ta_beta_u1'
        UNDER_ONE_FIVE='ta_beta_u1.5'
        UNDER_TWO='ta_beta_u2'
        OVER_ZERO='ta_beta_o0'
        OVER_ZERO_FIVE='ta_beta_o0.5'
        OVER_ONE='ta_beta_o1'
        OVER_ONE_FIVE='ta_beta_o1.5'
        OVER_TWO='ta_beta_o2'
        OVER_TWO_FIVE='ta_beta_o2.5'
        OVER_THREE='ta_beta_o3'
        OVER_FOUR='ta_beta_o4'
        ZERO_TO_ZERO_FIVE='ta_beta_0to0.5'
        ZERO_TO_ONE='ta_beta_0to1'
        ZERO_FIVE_TO_ONE='ta_beta_0.5to1'
        ZERO_FIVE_TO_ONE_FIVE='ta_beta_0.5to1.5'
        ONE_TO_ONE_FIVE='ta_beta_1to1.5'
        ONE_TO_TWO='ta_beta_1to2'

    def filter_beta(self, beta: Beta):
        self.filters['Beta'] = beta

    class AverageTrueRange(str, Enum):
        """
        A measure of stock volatility. The Average True Range is an exponential moving average (14-days) of the True Ranges. The range of a day's trading is high−low, True Range extends it to yesterday's closing price if it was outside of today's range, True Range =<br>max(high,closeprev) − min(low,closeprev)
        """
        OVER_ZERO_TWENTY_FIVE='ta_averagetruerange_o0.25'
        OVER_ZERO_FIVE='ta_averagetruerange_o0.5'
        OVER_ZERO_SEVENTY_FIVE='ta_averagetruerange_o0.75'
        OVER_ONE='ta_averagetruerange_o1'
        OVER_ONE_FIVE='ta_averagetruerange_o1.5'
        OVER_TWO='ta_averagetruerange_o2'
        OVER_TWO_FIVE='ta_averagetruerange_o2.5'
        OVER_THREE='ta_averagetruerange_o3'
        OVER_THREE_FIVE='ta_averagetruerange_o3.5'
        OVER_FOUR='ta_averagetruerange_o4'
        OVER_FOUR_FIVE='ta_averagetruerange_o4.5'
        OVER_FIVE='ta_averagetruerange_o5'
        UNDER_ZERO_TWENTY_FIVE='ta_averagetruerange_u0.25'
        UNDER_ZERO_FIVE='ta_averagetruerange_u0.5'
        UNDER_ZERO_SEVENTY_FIVE='ta_averagetruerange_u0.75'
        UNDER_ONE='ta_averagetruerange_u1'
        UNDER_ONE_FIVE='ta_averagetruerange_u1.5'
        UNDER_TWO='ta_averagetruerange_u2'
        UNDER_TWO_FIVE='ta_averagetruerange_u2.5'
        UNDER_THREE='ta_averagetruerange_u3'
        UNDER_THREE_FIVE='ta_averagetruerange_u3.5'
        UNDER_FOUR='ta_averagetruerange_u4'
        UNDER_FOUR_FIVE='ta_averagetruerange_u4.5'
        UNDER_FIVE='ta_averagetruerange_u5'

    def filter_average_true_range(self, average_true_range: AverageTrueRange):
        self.filters['AverageTrueRange'] = average_true_range

    class AverageVolume(str, Enum):
        """
        The average number of shares traded in a security per day.
        """
        UNDER_FIFTY_K='sh_avgvol_u50'
        UNDER_ONE_HUNDRED_K='sh_avgvol_u100'
        UNDER_FIVE_HUNDRED_K='sh_avgvol_u500'
        UNDER_SEVEN_HUNDRED_AND_FIFTY_K='sh_avgvol_u750'
        UNDER_ONE_M='sh_avgvol_u1000'
        OVER_FIFTY_K='sh_avgvol_o50'
        OVER_ONE_HUNDRED_K='sh_avgvol_o100'
        OVER_TWO_HUNDRED_K='sh_avgvol_o200'
        OVER_THREE_HUNDRED_K='sh_avgvol_o300'
        OVER_FOUR_HUNDRED_K='sh_avgvol_o400'
        OVER_FIVE_HUNDRED_K='sh_avgvol_o500'
        OVER_SEVEN_HUNDRED_AND_FIFTY_K='sh_avgvol_o750'
        OVER_ONE_M='sh_avgvol_o1000'
        OVER_TWO_M='sh_avgvol_o2000'
        ONE_HUNDRED_K_TO_FIVE_HUNDRED_K='sh_avgvol_100to500'
        ONE_HUNDRED_K_TO_ONE_M='sh_avgvol_100to1000'
        FIVE_HUNDRED_K_TO_ONE_M='sh_avgvol_500to1000'
        FIVE_HUNDRED_K_TO_TEN_M='sh_avgvol_500to10000'

    def filter_average_volume(self, average_volume: AverageVolume):
        self.filters['AverageVolume'] = average_volume

    class RelativeVolume(str, Enum):
        """
        Ratio between current volume and 3-month average, intraday adjusted.
        """
        OVER_TEN='sh_relvol_o10'
        OVER_FIVE='sh_relvol_o5'
        OVER_THREE='sh_relvol_o3'
        OVER_TWO='sh_relvol_o2'
        OVER_ONE_FIVE='sh_relvol_o1.5'
        OVER_ONE='sh_relvol_o1'
        OVER_ZERO_SEVENTY_FIVE='sh_relvol_o0.75'
        OVER_ZERO_FIVE='sh_relvol_o0.5'
        OVER_ZERO_TWENTY_FIVE='sh_relvol_o0.25'
        UNDER_TWO='sh_relvol_u2'
        UNDER_ONE_FIVE='sh_relvol_u1.5'
        UNDER_ONE='sh_relvol_u1'
        UNDER_ZERO_SEVENTY_FIVE='sh_relvol_u0.75'
        UNDER_ZERO_FIVE='sh_relvol_u0.5'
        UNDER_ZERO_TWENTY_FIVE='sh_relvol_u0.25'
        UNDER_ZERO_ONE='sh_relvol_u0.1'

    def filter_relative_volume(self, relative_volume: RelativeVolume):
        self.filters['RelativeVolume'] = relative_volume

    class PriceDollar(str, Enum):
        """
        The current stock price.
        """
        UNDER_DOLLAR_ONE='sh_price_u1'
        UNDER_DOLLAR_TWO='sh_price_u2'
        UNDER_DOLLAR_THREE='sh_price_u3'
        UNDER_DOLLAR_FOUR='sh_price_u4'
        UNDER_DOLLAR_FIVE='sh_price_u5'
        UNDER_DOLLAR_SEVEN='sh_price_u7'
        UNDER_DOLLAR_TEN='sh_price_u10'
        UNDER_DOLLAR_FIFTEEN='sh_price_u15'
        UNDER_DOLLAR_TWENTY='sh_price_u20'
        UNDER_DOLLAR_THIRTY='sh_price_u30'
        UNDER_DOLLAR_FORTY='sh_price_u40'
        UNDER_DOLLAR_FIFTY='sh_price_u50'
        OVER_DOLLAR_ONE='sh_price_o1'
        OVER_DOLLAR_TWO='sh_price_o2'
        OVER_DOLLAR_THREE='sh_price_o3'
        OVER_DOLLAR_FOUR='sh_price_o4'
        OVER_DOLLAR_FIVE='sh_price_o5'
        OVER_DOLLAR_SEVEN='sh_price_o7'
        OVER_DOLLAR_TEN='sh_price_o10'
        OVER_DOLLAR_FIFTEEN='sh_price_o15'
        OVER_DOLLAR_TWENTY='sh_price_o20'
        OVER_DOLLAR_THIRTY='sh_price_o30'
        OVER_DOLLAR_FORTY='sh_price_o40'
        OVER_DOLLAR_FIFTY='sh_price_o50'
        OVER_DOLLAR_SIXTY='sh_price_o60'
        OVER_DOLLAR_SEVENTY='sh_price_o70'
        OVER_DOLLAR_EIGHTY='sh_price_o80'
        OVER_DOLLAR_NINETY='sh_price_o90'
        OVER_DOLLAR_ONE_HUNDRED='sh_price_o100'
        DOLLAR_ONE_TO_DOLLAR_FIVE='sh_price_1to5'
        DOLLAR_ONE_TO_DOLLAR_TEN='sh_price_1to10'
        DOLLAR_ONE_TO_DOLLAR_TWENTY='sh_price_1to20'
        DOLLAR_FIVE_TO_DOLLAR_TEN='sh_price_5to10'
        DOLLAR_FIVE_TO_DOLLAR_TWENTY='sh_price_5to20'
        DOLLAR_FIVE_TO_DOLLAR_FIFTY='sh_price_5to50'
        DOLLAR_TEN_TO_DOLLAR_TWENTY='sh_price_10to20'
        DOLLAR_TEN_TO_DOLLAR_FIFTY='sh_price_10to50'
        DOLLAR_TWENTY_TO_DOLLAR_FIFTY='sh_price_20to50'
        DOLLAR_FIFTY_TO_DOLLAR_ONE_HUNDRED='sh_price_50to100'

    def filter_price_dollar(self, price_dollar: PriceDollar):
        self.filters['PriceDollar'] = price_dollar

    class TargetPrice(str, Enum):
        """
        Analysts' mean target price.
        """
        FIFTY_PERCENT_ABOVE_PRICE='targetprice_a50'
        FORTY_PERCENT_ABOVE_PRICE='targetprice_a40'
        THIRTY_PERCENT_ABOVE_PRICE='targetprice_a30'
        TWENTY_PERCENT_ABOVE_PRICE='targetprice_a20'
        TEN_PERCENT_ABOVE_PRICE='targetprice_a10'
        FIVE_PERCENT_ABOVE_PRICE='targetprice_a5'
        ABOVE_PRICE='targetprice_above'
        BELOW_PRICE='targetprice_below'
        FIVE_PERCENT_BELOW_PRICE='targetprice_b5'
        TEN_PERCENT_BELOW_PRICE='targetprice_b10'
        TWENTY_PERCENT_BELOW_PRICE='targetprice_b20'
        THIRTY_PERCENT_BELOW_PRICE='targetprice_b30'
        FORTY_PERCENT_BELOW_PRICE='targetprice_b40'
        FIFTY_PERCENT_BELOW_PRICE='targetprice_b50'

    def filter_target_price(self, target_price: TargetPrice):
        self.filters['TargetPrice'] = target_price

    class IpoDate(str, Enum):
        """
        Date when company had an IPO.
        """
        TODAY='ipodate_today'
        YESTERDAY='ipodate_yesterday'
        IN_THE_LAST_WEEK='ipodate_prevweek'
        IN_THE_LAST_MONTH='ipodate_prevmonth'
        IN_THE_LAST_QUARTER='ipodate_prevquarter'
        IN_THE_LAST_YEAR='ipodate_prevyear'
        IN_THE_LAST_TWO_YEARS='ipodate_prev2yrs'
        IN_THE_LAST_THREE_YEARS='ipodate_prev3yrs'
        IN_THE_LAST_FIVE_YEARS='ipodate_prev5yrs'
        MORE_THAN_A_YEAR_AGO='ipodate_more1'
        MORE_THAN_FIVE_YEARS_AGO='ipodate_more5'
        MORE_THAN_TEN_YEARS_AGO='ipodate_more10'
        MORE_THAN_FIFTEEN_YEARS_AGO='ipodate_more15'
        MORE_THAN_TWENTY_YEARS_AGO='ipodate_more20'
        MORE_THAN_TWENTY_FIVE_YEARS_AGO='ipodate_more25'

    def filter_ipo_date(self, ipo_date: IpoDate):
        self.filters['IpoDate'] = ipo_date

    class SharesOutstanding(str, Enum):
        """
        Shares outstanding represent the total number of shares issued by a corporation and held by its shareholders.
        """
        UNDER_ONE_M='sh_outstanding_u1'
        UNDER_FIVE_M='sh_outstanding_u5'
        UNDER_TEN_M='sh_outstanding_u10'
        UNDER_TWENTY_M='sh_outstanding_u20'
        UNDER_FIFTY_M='sh_outstanding_u50'
        UNDER_ONE_HUNDRED_M='sh_outstanding_u100'
        OVER_ONE_M='sh_outstanding_o1'
        OVER_TWO_M='sh_outstanding_o2'
        OVER_FIVE_M='sh_outstanding_o5'
        OVER_TEN_M='sh_outstanding_o10'
        OVER_TWENTY_M='sh_outstanding_o20'
        OVER_FIFTY_M='sh_outstanding_o50'
        OVER_ONE_HUNDRED_M='sh_outstanding_o100'
        OVER_TWO_HUNDRED_M='sh_outstanding_o200'
        OVER_FIVE_HUNDRED_M='sh_outstanding_o500'
        OVER_ONE_THOUSAND_M='sh_outstanding_o1000'

    def filter_shares_outstanding(self, shares_outstanding: SharesOutstanding):
        self.filters['SharesOutstanding'] = shares_outstanding

    class Float(str, Enum):
        """
        Float is the number of stock shares that are available for trading to the public. This doesn't include shares held by insiders.
        """
        UNDER_ONE_M='sh_float_u1'
        UNDER_FIVE_M='sh_float_u5'
        UNDER_TEN_M='sh_float_u10'
        UNDER_TWENTY_M='sh_float_u20'
        UNDER_FIFTY_M='sh_float_u50'
        UNDER_ONE_HUNDRED_M='sh_float_u100'
        OVER_ONE_M='sh_float_o1'
        OVER_TWO_M='sh_float_o2'
        OVER_FIVE_M='sh_float_o5'
        OVER_TEN_M='sh_float_o10'
        OVER_TWENTY_M='sh_float_o20'
        OVER_FIFTY_M='sh_float_o50'
        OVER_ONE_HUNDRED_M='sh_float_o100'
        OVER_TWO_HUNDRED_M='sh_float_o200'
        OVER_FIVE_HUNDRED_M='sh_float_o500'
        OVER_ONE_THOUSAND_M='sh_float_o1000'
        UNDER_TEN_PERCENT='sh_float_u10p'
        UNDER_TWENTY_PERCENT='sh_float_u20p'
        UNDER_THIRTY_PERCENT='sh_float_u30p'
        UNDER_FORTY_PERCENT='sh_float_u40p'
        UNDER_FIFTY_PERCENT='sh_float_u50p'
        UNDER_SIXTY_PERCENT='sh_float_u60p'
        UNDER_SEVENTY_PERCENT='sh_float_u70p'
        UNDER_EIGHTY_PERCENT='sh_float_u80p'
        UNDER_NINETY_PERCENT='sh_float_u90p'
        OVER_TEN_PERCENT='sh_float_o10p'
        OVER_TWENTY_PERCENT='sh_float_o20p'
        OVER_THIRTY_PERCENT='sh_float_o30p'
        OVER_FORTY_PERCENT='sh_float_o40p'
        OVER_FIFTY_PERCENT='sh_float_o50p'
        OVER_SIXTY_PERCENT='sh_float_o60p'
        OVER_SEVENTY_PERCENT='sh_float_o70p'
        OVER_EIGHTY_PERCENT='sh_float_o80p'
        OVER_NINETY_PERCENT='sh_float_o90p'

    def filter_float(self, float: Float):
        self.filters['Float'] = float

    class LatestNews(str, Enum):
        """
        Date of the latest reported news.
        """
        TODAY='news_date_today'
        AFTERMARKET_TODAY='news_date_todayafter'
        SINCE_YESTERDAY='news_date_sinceyesterday'
        SINCE_THE_AFTERMARKET_YESTERDAY='news_date_sinceyesterdayafter'
        YESTERDAY='news_date_yesterday'
        IN_THE_AFTERMARKET_YESTERDAY='news_date_yesterdayafter'
        IN_THE_LAST_FIVE_MINUTES='news_date_prevminutes5'
        IN_THE_LAST_THIRTY_MINUTES='news_date_prevminutes30'
        IN_THE_LAST_HOUR='news_date_prevhours1'
        IN_THE_LAST_TWENTY_FOUR_HOURS='news_date_prevhours24'
        IN_THE_LAST_SEVEN_DAYS='news_date_prevdays7'
        IN_THE_LAST_MONTH='news_date_prevmonth'

    def filter_latest_news(self, latest_news: LatestNews):
        self.filters['LatestNews'] = latest_news

    class AssetType(str, Enum):
        """
        The asset type of the ETF.
        """
        BONDS='etf_assettype_bonds'
        CARBON_TRADING='etf_assettype_carbontrading'
        CLOSED_END_FUNDS='etf_assettype_closedendfunds'
        COMMODITIES_AND_METALS='etf_assettype_commoditiesmetals'
        CRYPTOCURRENCY='etf_assettype_cryptocurrency'
        CURRENCY='etf_assettype_currency'
        EQUITIES_STOCKS='etf_assettype_equitiesstocks'
        EQUITIES_STOCKS_IPO_BASED='etf_assettype_equitiesstocksipobased'
        FREIGHT_FUTURES='etf_assettype_freightfutures'
        HEDGE_FUND_REPLICATION='etf_assettype_hedgefundreplication'
        MLP='etf_assettype_mlp'
        MULTI_ASSET_CONSERVATIVE='etf_assettype_multiassetconservative'
        MULTI_ASSET_GROWTH_AGGRESSIVE='etf_assettype_multiassetgrowthaggressive'
        MULTI_ASSET_MODERATE='etf_assettype_multiassetmoderate'
        MULTI_ASSET_TACTICAL_ACTIVE='etf_assettype_multiassettacticalactive'
        PREFERRED_STOCK='etf_assettype_preferredstock'
        PRIVATE_EQUITY='etf_assettype_privateequity'
        SPAC='etf_assettype_spac'

    def filter_asset_type(self, asset_type: AssetType):
        self.filters['AssetType'] = asset_type

    class Sponsor(str, Enum):
        """
        The fund manager (ETF) or issuing bank (ETN).
        """
        ABERDEEN='etf_sponsor_aberdeen'
        ABSOLUTE_INVESTMENT_ADVISERS='etf_sponsor_absoluteinvestmentadvisers'
        ACADEMY_AM='etf_sponsor_academyam'
        ACQUIRERS_FUNDS='etf_sponsor_acquirersfunds'
        ACRUENCE_CAPITAL='etf_sponsor_acruencecapital'
        ACSI_FUNDS='etf_sponsor_acsifunds'
        ACV_ETF='etf_sponsor_acvetf'
        ADAPTIV='etf_sponsor_adaptiv'
        ADAPTIVE_INVESTMENTS='etf_sponsor_adaptiveinvestments'
        ADASINA_SOCIAL_CAPITAL='etf_sponsor_adasinasocialcapital'
        ADVISOR_SHARES='etf_sponsor_advisorshares'
        ADVISORS_ASSET_MANAGEMENT='etf_sponsor_advisorsassetmanagement'
        ADVOCATE_CAPITAL_MANAGEMENT='etf_sponsor_advocatecapitalmanagement'
        AGFIQ='etf_sponsor_agfiq'
        ALEXIS_INVESTS='etf_sponsor_alexisinvests'
        ALGER='etf_sponsor_alger'
        ALLIANCEBERNSTEIN='etf_sponsor_alliancebernstein'
        ALLIANZIM='etf_sponsor_allianzim'
        ALPHA_ARCHITECT='etf_sponsor_alphaarchitect'
        ALPHAMARK='etf_sponsor_alphamark'
        ALPS='etf_sponsor_alps'
        ALTRIUS_CAPITAL='etf_sponsor_altriuscapital'
        ALTSHARES='etf_sponsor_altshares'
        AMERICAN_BEACON='etf_sponsor_americanbeacon'
        AMERICAN_CENTURY_INVESTMENTS='etf_sponsor_americancenturyinvestments'
        AMPLIFY_INVESTMENTS='etf_sponsor_amplifyinvestments'
        ANGEL_OAK='etf_sponsor_angeloak'
        AOT_INVEST='etf_sponsor_aotinvest'
        APPLIED_FINANCE_FUNDS='etf_sponsor_appliedfinancefunds'
        APTUS_CAPITAL_ADVISORS='etf_sponsor_aptuscapitaladvisors'
        ARGENT_CAPITAL_MANAGEMENT='etf_sponsor_argentcapitalmanagement'
        ARK_FUNDS='etf_sponsor_arkfunds'
        ARMADA_ETF_ADVISORS='etf_sponsor_armadaetfadvisors'
        ARROWSHARES='etf_sponsor_arrowshares'
        ASTORIA='etf_sponsor_astoria'
        ASYMSHARES='etf_sponsor_asymshares'
        ATAC_FUNDS='etf_sponsor_atacfunds'
        AVANTIS_INVESTORS='etf_sponsor_avantisinvestors'
        AXS_INVESTMENTS='etf_sponsor_axsinvestments'
        AZTLAN='etf_sponsor_aztlan'
        BAD_INVESTMENT='etf_sponsor_badinvestment'
        BAHL_AND_GAYNOR='etf_sponsor_bahlgaynor'
        BALLAST_AM='etf_sponsor_ballastam'
        BARCLAYS='etf_sponsor_barclays'
        BARCLAYS_IPATH='etf_sponsor_barclaysipath'
        BEACON='etf_sponsor_beacon'
        BEYOND_INVESTING='etf_sponsor_beyondinvesting'
        BITWISE='etf_sponsor_bitwise'
        BLACKROCK_ISHARES='etf_sponsor_blackrockishares'
        BLUEPRINT_FUND_MANAGEMENT='etf_sponsor_blueprintfundmanagement'
        BNY_MELLON='etf_sponsor_bnymellon'
        BONDBLOXX='etf_sponsor_bondbloxx'
        BRIDGES_CAPITAL='etf_sponsor_bridgescapital'
        BRIDGEWAY='etf_sponsor_bridgeway'
        BROOKSTONE='etf_sponsor_brookstone'
        BUILD_ASSET_MANAGEMENT='etf_sponsor_buildassetmanagement'
        BURNEY_INVESTMENT='etf_sponsor_burneyinvestment'
        BUSHIDO_CAPITAL='etf_sponsor_bushidocapital'
        CABANA_ETF='etf_sponsor_cabanaetf'
        CALAMOS_INVESTMENTS='etf_sponsor_calamosinvestments'
        CAMBIAR_INVESTORS='etf_sponsor_cambiarinvestors'
        CAMBRIA_FUNDS='etf_sponsor_cambriafunds'
        CAPITAL_GROUP='etf_sponsor_capitalgroup'
        CARBON_COLLECTIVE='etf_sponsor_carboncollective'
        CARBON_FUND_ADVISORS='etf_sponsor_carbonfundadvisors'
        CBOE_VEST='etf_sponsor_cboevest'
        CHANGEBRIDGE_CAPITAL='etf_sponsor_changebridgecapital'
        CLOCKWISE_CAPITAL='etf_sponsor_clockwisecapital'
        CLOUTY='etf_sponsor_clouty'
        CNIC_FUNDS='etf_sponsor_cnicfunds'
        COLUMBIA_MANAGEMENT='etf_sponsor_columbiamanagement'
        CONDUCTOR_ETF='etf_sponsor_conductoretf'
        CONGRESS_AMC='etf_sponsor_congressamc'
        CONVERGENCE_INVESTMENT_PARTNERS='etf_sponsor_convergenceinvestmentpartners'
        CONVEXITYSHARES='etf_sponsor_convexityshares'
        CORNERCAP='etf_sponsor_cornercap'
        COUNTERPOINT_MUTUAL_FUNDS='etf_sponsor_counterpointmutualfunds'
        CREDIT_SUISSE='etf_sponsor_creditsuisse'
        CROSSINGBRIDGE='etf_sponsor_crossingbridge'
        CULTIVAR_FUNDS='etf_sponsor_cultivarfunds'
        DAVIS_ADVISORS='etf_sponsor_davisadvisors'
        DAY_HAGAN='etf_sponsor_dayhagan'
        DAYS_GLOBAL_ADVISORS='etf_sponsor_daysglobaladvisors'
        DEFIANCE_ETFS='etf_sponsor_defianceetfs'
        DEMOCRACY_INVESTMENTS='etf_sponsor_democracyinvestments'
        DIMENSIONAL='etf_sponsor_dimensional'
        DIREXION_SHARES='etf_sponsor_direxionshares'
        DISCIPLINE_FUND='etf_sponsor_disciplinefund'
        DISTILLATE_CAPITAL='etf_sponsor_distillatecapital'
        DOUBLELINE_FUNDS='etf_sponsor_doublelinefunds'
        DRIVEWEALTH='etf_sponsor_drivewealth'
        DWS='etf_sponsor_dws'
        DYNAMIC_SHARES='etf_sponsor_dynamicshares'
        ECOFIN='etf_sponsor_ecofin'
        ELEMENT_FUNDS='etf_sponsor_elementfunds'
        ELEVATE_SHARES='etf_sponsor_elevateshares'
        ENGINE_NO_ONE='etf_sponsor_engineno1'
        ENTREPRENEURSHARES='etf_sponsor_entrepreneurshares'
        ENVESTNET='etf_sponsor_envestnet'
        ETF_MANAGERS_GROUP='etf_sponsor_etfmanagersgroup'
        EUCLID_ETF='etf_sponsor_euclidetf'
        EVOKE_ADVISORS='etf_sponsor_evokeadvisors'
        EXCHANGE_TRADED_CONCEPTS='etf_sponsor_exchangetradedconcepts'
        F_M_INVESTMENTS='etf_sponsor_fminvestments'
        FAIRLEAD_STRATEGIES='etf_sponsor_fairleadstrategies'
        FCF_ADVISORS='etf_sponsor_fcfadvisors'
        FEDERATED_HERMES='etf_sponsor_federatedhermes'
        FIDELITY='etf_sponsor_fidelity'
        FIRST_MANHATTAN='etf_sponsor_firstmanhattan'
        FIRST_PACIFIC_ADVISORS='etf_sponsor_firstpacificadvisors'
        FIRST_TRUST='etf_sponsor_firsttrust'
        FIS='etf_sponsor_fis'
        FLEXSHARES_NORTHERN_TRUST='etf_sponsor_flexsharesnortherntrust'
        FOLIOBEYOND='etf_sponsor_foliobeyond'
        FORMIDABLE_FUNDS='etf_sponsor_formidablefunds'
        FORMULAFOLIO_INVESTMENTS='etf_sponsor_formulafolioinvestments'
        FRANKLIN_TEMPLETON='etf_sponsor_franklintempleton'
        FREEDOM_DAY='etf_sponsor_freedomday'
        FUNDX='etf_sponsor_fundx'
        FUTURE_FUNDS='etf_sponsor_futurefunds'
        GADSDEN='etf_sponsor_gadsden'
        GAMCO_INVESTORS='etf_sponsor_gamcoinvestors'
        GAVEKAL_CAPITAL='etf_sponsor_gavekalcapital'
        GLOBAL_X='etf_sponsor_globalx'
        GOD_BLESS='etf_sponsor_godbless'
        GOLDMAN_SACHS='etf_sponsor_goldmansachs'
        GOOSE_HOLLOW='etf_sponsor_goosehollow'
        GOTHAM_ETF='etf_sponsor_gothametf'
        GRANITESHARES='etf_sponsor_graniteshares'
        GRAYSCALE='etf_sponsor_grayscale'
        GRIZZLE='etf_sponsor_grizzle'
        GURU_FOCUS='etf_sponsor_gurufocus'
        HARBOR_FUNDS='etf_sponsor_harborfunds'
        HARTFORD_FUNDS='etf_sponsor_hartfordfunds'
        HASHDEX='etf_sponsor_hashdex'
        HENNESSY_FUNDS='etf_sponsor_hennessyfunds'
        HORIZON_KINETICS='etf_sponsor_horizonkinetics'
        HOWARD_CAPITAL_MANAGEMENT='etf_sponsor_howardcapitalmanagement'
        HOYA_CAPITAL='etf_sponsor_hoyacapital'
        HUMANKIND='etf_sponsor_humankind'
        HYPATIA_CAPITAL='etf_sponsor_hypatiacapital'
        IMGP_GLOBAL_PARTNER='etf_sponsor_imgpglobalpartner'
        IMPACT_SHARES='etf_sponsor_impactshares'
        INDEX_IQ='etf_sponsor_indexiq'
        INFRASTRUCTURE_CAPITAL_ADVISORS='etf_sponsor_infrastructurecapitaladvisors'
        INNOVATIVE_PORTFOLIOS='etf_sponsor_innovativeportfolios'
        INNOVATOR_MANAGEMENT='etf_sponsor_innovatormanagement'
        INSPIRE_INVESTING='etf_sponsor_inspireinvesting'
        INVESCO='etf_sponsor_invesco'
        IONIC_CAPITAL_MANAGEMENT='etf_sponsor_ioniccapitalmanagement'
        JACOB_FUNDS='etf_sponsor_jacobfunds'
        JANUS='etf_sponsor_janus'
        JOHN_HANCOCK_FUNDS='etf_sponsor_johnhancockfunds'
        JPMORGAN_CHASE='etf_sponsor_jpmorganchase'
        KAIJU_ETF_ADVISORS='etf_sponsor_kaijuetfadvisors'
        KELLY_ETFS='etf_sponsor_kellyetfs'
        KINGSBARN_CAPITAL='etf_sponsor_kingsbarncapital'
        KOVITZ='etf_sponsor_kovitz'
        KRANE_SHARES='etf_sponsor_kraneshares'
        LAFFER_TENGLER='etf_sponsor_laffertengler'
        LEADERSHARES='etf_sponsor_leadershares'
        LEATHERBACK_ASSET_MANAGEMENT='etf_sponsor_leatherbackassetmanagement'
        LEUTHOLD_GROUP='etf_sponsor_leutholdgroup'
        LIQUID_STRATEGIES='etf_sponsor_liquidstrategies'
        LITTLE_HARBOR_ADVISORS='etf_sponsor_littleharboradvisors'
        LOGAN_CAPITAL='etf_sponsor_logancapital'
        LYRICAL_AM='etf_sponsor_lyricalam'
        MADISON_FUNDS='etf_sponsor_madisonfunds'
        MAIN_MANAGEMENT='etf_sponsor_mainmanagement'
        MAIRS_AND_POWER='etf_sponsor_mairspower'
        MATTHEWS_ASIA='etf_sponsor_matthewsasia'
        MAX_ETNS='etf_sponsor_maxetns'
        MCELHENNY_SHEFFIELD='etf_sponsor_mcelhennysheffield'
        MEET_KEVIN='etf_sponsor_meetkevin'
        MERK_INVESTMENTS='etf_sponsor_merkinvestments'
        MERLYN_AI='etf_sponsor_merlynai'
        MICROSECTORS='etf_sponsor_microsectors'
        MKAM_ETF='etf_sponsor_mkametf'
        MOHR_FUNDS='etf_sponsor_mohrfunds'
        MONARCH_FUNDS='etf_sponsor_monarchfunds'
        MORGAN_DEMPSEY='etf_sponsor_morgandempsey'
        MORGAN_STANLEY='etf_sponsor_morganstanley'
        MOTLEY_FOOL_ASSET_MANAGEMENT='etf_sponsor_motleyfoolassetmanagement'
        MUSQ='etf_sponsor_musq'
        NATIONWIDE='etf_sponsor_nationwide'
        NATIXIS='etf_sponsor_natixis'
        NEOS_FUNDS='etf_sponsor_neosfunds'
        NEUBERGER_BERMAN='etf_sponsor_neubergerberman'
        NEWDAY='etf_sponsor_newday'
        NUVEEN='etf_sponsor_nuveen'
        ONEASCENT_INVESTMENTS='etf_sponsor_oneascentinvestments'
        OPTIMIZE_ADVISORS='etf_sponsor_optimizeadvisors'
        PACER_FINANCIAL='etf_sponsor_pacerfinancial'
        PANAGRAM='etf_sponsor_panagram'
        PARABLA='etf_sponsor_parabla'
        PARALEL_ADVISORS='etf_sponsor_paraleladvisors'
        PGIM_INVESTMENTS='etf_sponsor_pgiminvestments'
        PIMCO='etf_sponsor_pimco'
        PINNACLE_DYNAMIC_FUNDS='etf_sponsor_pinnacledynamicfunds'
        PMV_CAPITAL='etf_sponsor_pmvcapital'
        POINT_BRIDGE_CAPITAL='etf_sponsor_pointbridgecapital'
        PRINCIPAL_FINANCIAL_SERVICES='etf_sponsor_principalfinancialservices'
        PROCUREAM='etf_sponsor_procuream'
        PROSHARES='etf_sponsor_proshares'
        PUTNAM_INVESTMENTS='etf_sponsor_putnaminvestments'
        Q_THREE_ALL_SEASON='etf_sponsor_q3allseason'
        QRAFT_TECHNOLOGIES='etf_sponsor_qrafttechnologies'
        R_THREE_GLOBAL_CAPITAL='etf_sponsor_r3globalcapital'
        RAREVIEW_FUNDS='etf_sponsor_rareviewfunds'
        RAYLIANT='etf_sponsor_rayliant'
        REFLECTION_ASSET_MANAGEMENT='etf_sponsor_reflectionassetmanagement'
        REGENTS_PARK_FUNDS='etf_sponsor_regentsparkfunds'
        RELATIVE_SENTIMENT='etf_sponsor_relativesentiment'
        RENAISSANCE='etf_sponsor_renaissance'
        RETURNED_STACK='etf_sponsor_returnedstack'
        REVERB='etf_sponsor_reverb'
        ROBINSON_CAPITAL='etf_sponsor_robinsoncapital'
        ROC_INVESTMENTS='etf_sponsor_rocinvestments'
        ROUNDHILL_FINANCIAL='etf_sponsor_roundhillfinancial'
        RUNNING_OAK='etf_sponsor_runningoak'
        SABA_CAPITAL='etf_sponsor_sabacapital'
        SCHWAB='etf_sponsor_schwab'
        SEGALL_BRYANT_AND_HAMILL='etf_sponsor_segallbryanthamill'
        SEI_INVESTMENTS_COMPANY='etf_sponsor_seiinvestmentscompany'
        SIMPLIFY_ETF='etf_sponsor_simplifyetf'
        SIREN_ETF='etf_sponsor_sirenetf'
        SMARTETFS='etf_sponsor_smartetfs'
        SOFI='etf_sponsor_sofi'
        SONICSHARES='etf_sponsor_sonicshares'
        SOUND_ETF='etf_sponsor_soundetf'
        SOUNDWATCH='etf_sponsor_soundwatch'
        SPARKLINE_CAPITAL='etf_sponsor_sparklinecapital'
        SPEAR_INVEST='etf_sponsor_spearinvest'
        SPFUNDS='etf_sponsor_spfunds'
        SPINNAKER_ETF_TRUST='etf_sponsor_spinnakeretftrust'
        SPROTT_ASSET_MANAGEMENT='etf_sponsor_sprottassetmanagement'
        STATE_STREET_SPDR='etf_sponsor_statestreetspdr'
        STERLING_CAPITAL='etf_sponsor_sterlingcapital'
        STF_MANAGEMENT='etf_sponsor_stfmanagement'
        STRATEGAS_ASSET_MANAGEMENT='etf_sponsor_strategasassetmanagement'
        STRATEGY_SHARES='etf_sponsor_strategyshares'
        STRIVE_ASSET_MANAGEMENT='etf_sponsor_striveassetmanagement'
        SUBVERSIVE_ETFS='etf_sponsor_subversiveetfs'
        SUMMIT_GLOBAL_INVESTMENTS='etf_sponsor_summitglobalinvestments'
        SWAN_GLOBAL_INVESTMENTS='etf_sponsor_swanglobalinvestments'
        SYNTAX='etf_sponsor_syntax'
        T_ROWE_PRICE='etf_sponsor_troweprice'
        TACTICAL_ADVANTAGE='etf_sponsor_tacticaladvantage'
        TEMA='etf_sponsor_tema'
        TEUCRIUM='etf_sponsor_teucrium'
        TEXAS_CAPITAL='etf_sponsor_texascapital'
        THOR_FINANCIAL_TECHNOLOGIES='etf_sponsor_thorfinancialtechnologies'
        THRIVENT='etf_sponsor_thrivent'
        TIMOTHY_PLAN='etf_sponsor_timothyplan'
        TOEWS_FUNDS='etf_sponsor_toewsfunds'
        TORTOISE_CAPITAL_ADVISORS='etf_sponsor_tortoisecapitaladvisors'
        TOUCHSTONE_INVESTMENTS='etf_sponsor_touchstoneinvestments'
        TRAJAN_WEALTH='etf_sponsor_trajanwealth'
        TRUESHARES='etf_sponsor_trueshares'
        TUTTLE_TACTICAL_MANAGEMENT='etf_sponsor_tuttletacticalmanagement'
        U_S_GLOBAL_INVESTORS='etf_sponsor_usglobalinvestors'
        UBS='etf_sponsor_ubs'
        UNITED_STATES_COMMODITY_FUNDS='etf_sponsor_unitedstatescommodityfunds'
        UNLIMITED='etf_sponsor_unlimited'
        V_SQUARE='etf_sponsor_vsquare'
        VALIDUS='etf_sponsor_validus'
        VALKYRIE_FUNDS='etf_sponsor_valkyriefunds'
        VAN_ECK_ASSOCIATES_CORPORATION='etf_sponsor_vaneckassociatescorporation'
        VANGUARD='etf_sponsor_vanguard'
        VEGTECH='etf_sponsor_vegtech'
        VERIDIEN='etf_sponsor_veridien'
        VESPER_CAPITAL_MANAGEMENT='etf_sponsor_vespercapitalmanagement'
        VICTORYSHARES='etf_sponsor_victoryshares'
        VIDENT='etf_sponsor_vident'
        VIRTUS_ETF_SOLUTIONS='etf_sponsor_virtusetfsolutions'
        VOLATILITY_SHARES='etf_sponsor_volatilityshares'
        WAHED_INVEST='etf_sponsor_wahedinvest'
        WBI_SHARES='etf_sponsor_wbishares'
        WEALTH_TRUST='etf_sponsor_wealthtrust'
        WISDOM_TREE='etf_sponsor_wisdomtree'
        X_SQUARE_ETF='etf_sponsor_xsquareetf'
        XFUNDS='etf_sponsor_xfunds'
        ZACKS='etf_sponsor_zacks'
        ZEGA_ETF='etf_sponsor_zegaetf'

    def filter_sponsor(self, sponsor: Sponsor):
        self.filters['Sponsor'] = sponsor

    class NetExpenseRatio(str, Enum):
        """
        Gross expense net of fee waivers, as a % of net assets as published by the ETF Issuer.
        """
        UNDER_ZERO_ONE_PERCENT='etf_netexpense_u01'
        UNDER_ZERO_TWO_PERCENT='etf_netexpense_u02'
        UNDER_ZERO_THREE_PERCENT='etf_netexpense_u03'
        UNDER_ZERO_FOUR_PERCENT='etf_netexpense_u04'
        UNDER_ZERO_FIVE_PERCENT='etf_netexpense_u05'
        UNDER_ZERO_SIX_PERCENT='etf_netexpense_u06'
        UNDER_ZERO_SEVEN_PERCENT='etf_netexpense_u07'
        UNDER_ZERO_EIGHT_PERCENT='etf_netexpense_u08'
        UNDER_ZERO_NINE_PERCENT='etf_netexpense_u09'
        UNDER_ONE_ZERO_PERCENT='etf_netexpense_u10'

    def filter_net_expense_ratio(self, net_expense_ratio: NetExpenseRatio):
        self.filters['NetExpenseRatio'] = net_expense_ratio

    class NetFundFlows(str, Enum):
        """
        Net Fund Flows of the ETF as percentage of Assets Under Management
        """
        ONE_MONTH_OVER_ZERO_PERCENT='etf_fundflows_1mo0'
        ONE_MONTH_OVER_TEN_PERCENT='etf_fundflows_1mo10'
        ONE_MONTH_OVER_TWENTY_FIVE_PERCENT='etf_fundflows_1mo25'
        ONE_MONTH_OVER_FIFTY_PERCENT='etf_fundflows_1mo50'
        ONE_MONTH_UNDER_ZERO_PERCENT='etf_fundflows_1mu0'
        ONE_MONTH_UNDER_TEN_PERCENT='etf_fundflows_1mu10'
        ONE_MONTH_UNDER_TWENTY_FIVE_PERCENT='etf_fundflows_1mu25'
        ONE_MONTH_UNDER_FIFTY_PERCENT='etf_fundflows_1mu50'
        THREE_MONTH_OVER_ZERO_PERCENT='etf_fundflows_3mo0'
        THREE_MONTH_OVER_TEN_PERCENT='etf_fundflows_3mo10'
        THREE_MONTH_OVER_TWENTY_FIVE_PERCENT='etf_fundflows_3mo25'
        THREE_MONTH_OVER_FIFTY_PERCENT='etf_fundflows_3mo50'
        THREE_MONTH_UNDER_ZERO_PERCENT='etf_fundflows_3mu0'
        THREE_MONTH_UNDER_TEN_PERCENT='etf_fundflows_3mu10'
        THREE_MONTH_UNDER_TWENTY_FIVE_PERCENT='etf_fundflows_3mu25'
        THREE_MONTH_UNDER_FIFTY_PERCENT='etf_fundflows_3mu50'
        YTD_OVER_ZERO_PERCENT='etf_fundflows_ytdo0'
        YTD_OVER_TEN_PERCENT='etf_fundflows_ytdo10'
        YTD_OVER_TWENTY_FIVE_PERCENT='etf_fundflows_ytdo25'
        YTD_OVER_FIFTY_PERCENT='etf_fundflows_ytdo50'
        YTD_UNDER_ZERO_PERCENT='etf_fundflows_ytdu0'
        YTD_UNDER_TEN_PERCENT='etf_fundflows_ytdu10'
        YTD_UNDER_TWENTY_FIVE_PERCENT='etf_fundflows_ytdu25'
        YTD_UNDER_FIFTY_PERCENT='etf_fundflows_ytdu50'

    def filter_net_fund_flows(self, net_fund_flows: NetFundFlows):
        self.filters['NetFundFlows'] = net_fund_flows

    class AnnualizedReturn(str, Enum):
        """
        Annualized rate of Return of the ETF.
        """
        ONE_YEAR_OVER_ZERO_PERCENT='etf_return_1yo0'
        ONE_YEAR_OVER_FIVE_PERCENT='etf_return_1yo05'
        ONE_YEAR_OVER_TEN_PERCENT='etf_return_1yo10'
        ONE_YEAR_OVER_TWENTY_FIVE_PERCENT='etf_return_1yo25'
        ONE_YEAR_UNDER_ZERO_PERCENT='etf_return_1yu0'
        ONE_YEAR_UNDER_FIVE_PERCENT='etf_return_1yu05'
        ONE_YEAR_UNDER_TEN_PERCENT='etf_return_1yu10'
        ONE_YEAR_UNDER_TWENTY_FIVE_PERCENT='etf_return_1yu25'
        THREE_YEAR_OVER_ZERO_PERCENT='etf_return_3yo0'
        THREE_YEAR_OVER_FIVE_PERCENT='etf_return_3yo05'
        THREE_YEAR_OVER_TEN_PERCENT='etf_return_3yo10'
        THREE_YEAR_OVER_TWENTY_FIVE_PERCENT='etf_return_3yo25'
        THREE_YEAR_UNDER_ZERO_PERCENT='etf_return_3yu0'
        THREE_YEAR_UNDER_FIVE_PERCENT='etf_return_3yu05'
        THREE_YEAR_UNDER_TEN_PERCENT='etf_return_3yu10'
        THREE_YEAR_UNDER_TWENTY_FIVE_PERCENT='etf_return_3yu25'
        FIVE_YEAR_OVER_ZERO_PERCENT='etf_return_5yo0'
        FIVE_YEAR_OVER_FIVE_PERCENT='etf_return_5yo05'
        FIVE_YEAR_OVER_TEN_PERCENT='etf_return_5yo10'
        FIVE_YEAR_OVER_TWENTY_FIVE_PERCENT='etf_return_5yo25'
        FIVE_YEAR_UNDER_ZERO_PERCENT='etf_return_5yu0'
        FIVE_YEAR_UNDER_FIVE_PERCENT='etf_return_5yu05'
        FIVE_YEAR_UNDER_TEN_PERCENT='etf_return_5yu10'
        FIVE_YEAR_UNDER_TWENTY_FIVE_PERCENT='etf_return_5yu25'

    def filter_annualized_return(self, annualized_return: AnnualizedReturn):
        self.filters['AnnualizedReturn'] = annualized_return

    class Tags(str, Enum):
        """
        Various ETF tags.
        """
        THIRTEEN_F='etf_tags_13f'
        THREE_D_PRINTING='etf_tags_3dprinting'
        FIVE_G='etf_tags_5g'
        A_I='etf_tags_ai'
        AAPL='etf_tags_aapl'
        AEROSPACE_DEFENSE='etf_tags_aerospacedefense'
        AFRICA='etf_tags_africa'
        AGGRESSIVE='etf_tags_aggressive'
        AGRICULTURE='etf_tags_agriculture'
        AIRCRAFT='etf_tags_aircraft'
        AIRLINES='etf_tags_airlines'
        ALCOHOL_TOBACCO='etf_tags_alcoholtobacco'
        AMD='etf_tags_amd'
        AMZN='etf_tags_amzn'
        ARGENTINA='etf_tags_argentina'
        ARKK='etf_tags_arkk'
        ASIA='etf_tags_asia'
        ASIA_EX_JAPAN='etf_tags_asiaexjapan'
        ASIA_PACIFIC='etf_tags_asiapacific'
        ASIA_PACIFIC_EX_JAPAN='etf_tags_asiapacificexjapan'
        ASSET_ROTATION='etf_tags_assetrotation'
        AUD='etf_tags_aud'
        AUSTRALIA='etf_tags_australia'
        AUSTRIA='etf_tags_austria'
        AUTO_INDUSTRY='etf_tags_autoindustry'
        AUTOMATION='etf_tags_automation'
        AUTONOMOUS_VEHICLES='etf_tags_autonomousvehicles'
        BABA='etf_tags_baba'
        BANKS='etf_tags_banks'
        BATTERIES='etf_tags_batteries'
        BDC='etf_tags_bdc'
        BELGIUM='etf_tags_belgium'
        BETTING='etf_tags_betting'
        BIG_DATA='etf_tags_bigdata'
        BIOTECHNOLOGY='etf_tags_biotechnology'
        BITCOIN='etf_tags_bitcoin'
        BLOCKCHAIN='etf_tags_blockchain'
        BLUE_CHIP='etf_tags_bluechip'
        BONDS='etf_tags_bonds'
        BRAZIL='etf_tags_brazil'
        BROKERAGE='etf_tags_brokerage'
        BUFFER='etf_tags_buffer'
        BUYBACK='etf_tags_buyback'
        CAD='etf_tags_cad'
        CANADA='etf_tags_canada'
        CANCER='etf_tags_cancer'
        CANNABIS='etf_tags_cannabis'
        CAPITAL_MARKETS='etf_tags_capitalmarkets'
        CARBON_ALLOWANCES='etf_tags_carbonallowances'
        CARBON_LOW='etf_tags_carbonlow'
        CASH_COW='etf_tags_cashcow'
        CASINO='etf_tags_casino'
        CATHOLIC_VALUES='etf_tags_catholicvalues'
        CHF='etf_tags_chf'
        CHILE='etf_tags_chile'
        CHINA='etf_tags_china'
        CLEAN_ENERGY='etf_tags_cleanenergy'
        CLIMATE_CHANGE='etf_tags_climatechange'
        CLINICAL_TRIALS='etf_tags_clinicaltrials'
        CLO='etf_tags_clo'
        CLOUD_COMPUTING='etf_tags_cloudcomputing'
        COBALT='etf_tags_cobalt'
        COIN='etf_tags_coin'
        COLOMBIA='etf_tags_colombia'
        COMMODITY='etf_tags_commodity'
        COMMUNICATION_SERVICES='etf_tags_communicationservices'
        COMMUNITY_BANKS='etf_tags_communitybanks'
        CONSERVATIVE='etf_tags_conservative'
        CONSUMER='etf_tags_consumer'
        CONSUMER_DISCRETIONARY='etf_tags_consumerdiscretionary'
        CONSUMER_STAPLES='etf_tags_consumerstaples'
        CONVERTIBLE_SECURITIES='etf_tags_convertiblesecurities'
        COPPER='etf_tags_copper'
        CORN='etf_tags_corn'
        CORPORATE_BONDS='etf_tags_corporatebonds'
        COVERED_CALL='etf_tags_coveredcall'
        CRYPTO='etf_tags_crypto'
        CRYPTO_SPOT='etf_tags_cryptospot'
        CURRENCIES='etf_tags_currencies'
        CURRENCY='etf_tags_currency'
        CURRENCY_BONDS='etf_tags_currencybonds'
        CUSTOMER='etf_tags_customer'
        CYBER_SECURITY='etf_tags_cybersecurity'
        DATA_CENTERS='etf_tags_datacenters'
        DAX='etf_tags_dax'
        DEBT='etf_tags_debt'
        DEBT_SECURITIES='etf_tags_debtsecurities'
        DEMOCRATS='etf_tags_democrats'
        DENMARK='etf_tags_denmark'
        DERIVATIVES='etf_tags_derivatives'
        DEVELOPED='etf_tags_developed'
        DEVELOPED_EX_JAPAN='etf_tags_developedexjapan'
        DEVELOPED_EX_U_S='etf_tags_developedexus'
        DIGITAL_INFRASTRUCTURE='etf_tags_digitalinfrastructure'
        DIGITAL_PAYMENTS='etf_tags_digitalpayments'
        DIS='etf_tags_dis'
        DISASTER_RECOVERY='etf_tags_disasterrecovery'
        DISRUPTIVE='etf_tags_disruptive'
        DIVIDEND='etf_tags_dividend'
        DIVIDEND_GROWTH='etf_tags_dividendgrowth'
        DIVIDEND_WEIGHT='etf_tags_dividendweight'
        DJIA='etf_tags_djia'
        DRY_BULK='etf_tags_drybulk'
        E_COMMERCE='etf_tags_ecommerce'
        E_SPORTS='etf_tags_esports'
        EAFE='etf_tags_eafe'
        EDUCATION='etf_tags_education'
        EGYPT='etf_tags_egypt'
        ELECTRIC_VEHICLES='etf_tags_electricvehicles'
        ELECTRICITY='etf_tags_electricity'
        EMERGING='etf_tags_emerging'
        EMERGING_EX_CHINA='etf_tags_emergingexchina'
        ENERGY='etf_tags_energy'
        ENERGY_MANAGEMENT='etf_tags_energymanagement'
        ENERGY_PRODUCERS='etf_tags_energyproducers'
        ENERGY_STORAGE='etf_tags_energystorage'
        ENTERTAINMENT='etf_tags_entertainment'
        ENVIRONMENTAL='etf_tags_environmental'
        EQUAL_WEIGHT='etf_tags_equalweight'
        EQUITY='etf_tags_equity'
        ESG='etf_tags_esg'
        ETFS='etf_tags_etfs'
        ETHEREUM='etf_tags_ethereum'
        EUR='etf_tags_eur'
        EUROPE='etf_tags_europe'
        EUROZONE='etf_tags_eurozone'
        EX_ENERGY='etf_tags_exenergy'
        EX_FINANCIAL='etf_tags_exfinancial'
        EX_FOSSIL_FUELS='etf_tags_exfossilfuels'
        EX_HEALTHCARE='etf_tags_exhealthcare'
        EX_TECHNOLOGY='etf_tags_extechnology'
        EXCHANGES='etf_tags_exchanges'
        FACTOR_ROTATION='etf_tags_factorrotation'
        FANG='etf_tags_fang'
        FINANCIAL='etf_tags_financial'
        FINLAND='etf_tags_finland'
        FINTECH='etf_tags_fintech'
        FIXED_INCOME='etf_tags_fixedincome'
        FIXED_PERIOD='etf_tags_fixedperiod'
        FLOATING_RATE='etf_tags_floatingrate'
        FOOD='etf_tags_food'
        FOOD_BEVERAGE='etf_tags_foodbeverage'
        FOSSIL_FUELS='etf_tags_fossilfuels'
        FRANCE='etf_tags_france'
        FUNDAMENTAL='etf_tags_fundamental'
        FUNDAMENTAL_WEIGHT='etf_tags_fundamentalweight'
        FUTURES='etf_tags_futures'
        GAMING='etf_tags_gaming'
        GBP='etf_tags_gbp'
        GENDER='etf_tags_gender'
        GENOMICS='etf_tags_genomics'
        GERMANY='etf_tags_germany'
        GLD='etf_tags_gld'
        GLOBAL='etf_tags_global'
        GLOBAL_EX_U_S='etf_tags_globalexus'
        GOLD='etf_tags_gold'
        GOLD_MINERS='etf_tags_goldminers'
        GOOGL='etf_tags_googl'
        GOVERNMENT_BONDS='etf_tags_governmentbonds'
        GREECE='etf_tags_greece'
        GROWTH='etf_tags_growth'
        HARDWARE='etf_tags_hardware'
        HEALTHCARE='etf_tags_healthcare'
        HEDGE_CURRENCY='etf_tags_hedgecurrency'
        HEDGE_FUND='etf_tags_hedgefund'
        HEDGE_INFLATION='etf_tags_hedgeinflation'
        HEDGE_RATES='etf_tags_hedgerates'
        HEDGE_RISK='etf_tags_hedgerisk'
        HIGH_BETA='etf_tags_highbeta'
        HIGH_YIELD='etf_tags_highyield'
        HOME_CONSTRUCTION='etf_tags_homeconstruction'
        HOME_OFFICE='etf_tags_homeoffice'
        HONK_KONG='etf_tags_honkkong'
        HOTEL='etf_tags_hotel'
        HYDROGEN='etf_tags_hydrogen'
        I_T='etf_tags_it'
        INCOME='etf_tags_income'
        INDIA='etf_tags_india'
        INDONESIA='etf_tags_indonesia'
        INDUSTRIALS='etf_tags_industrials'
        INFLATION='etf_tags_inflation'
        INFRASTRUCTURE='etf_tags_infrastructure'
        INNOVATION='etf_tags_innovation'
        INSURANCE='etf_tags_insurance'
        INTERNATIONAL='etf_tags_international'
        INTERNET='etf_tags_internet'
        INTERNET_OF_THINGS='etf_tags_internetofthings'
        INVERSE='etf_tags_inverse'
        INVESTMENT_GRADE='etf_tags_investmentgrade'
        IPO='etf_tags_ipo'
        IRELAND='etf_tags_ireland'
        ISRAEL='etf_tags_israel'
        ITALY='etf_tags_italy'
        JAPAN='etf_tags_japan'
        JIM_CRAMER='etf_tags_jimcramer'
        JPM='etf_tags_jpm'
        JPY='etf_tags_jpy'
        KUWAIT='etf_tags_kuwait'
        LARGE_CAP='etf_tags_largecap'
        LATIN_AMERICA='etf_tags_latinamerica'
        LEADERSHIP='etf_tags_leadership'
        LEVERAGE='etf_tags_leverage'
        LIFESTYLE='etf_tags_lifestyle'
        LITHIUM='etf_tags_lithium'
        LOANS='etf_tags_loans'
        LONG_SHORT='etf_tags_longshort'
        LUXURY='etf_tags_luxury'
        M_AND_A='etf_tags_ma'
        MACHINE_LEARNING='etf_tags_machinelearning'
        MACRO='etf_tags_macro'
        MALAYSIA='etf_tags_malaysia'
        MARKET_SENTIMENT='etf_tags_marketsentiment'
        MARKETING='etf_tags_marketing'
        MATERIALS='etf_tags_materials'
        MBS='etf_tags_mbs'
        MEDIA='etf_tags_media'
        MEDICAL='etf_tags_medical'
        MEGA_CAP='etf_tags_megacap'
        META='etf_tags_meta'
        METALS='etf_tags_metals'
        METAVERSE='etf_tags_metaverse'
        MEXICO='etf_tags_mexico'
        MICRO_CAP='etf_tags_microcap'
        MID_CAP='etf_tags_midcap'
        MID_LARGE_CAP='etf_tags_midlargecap'
        MIDSTREAM='etf_tags_midstream'
        MILITARY='etf_tags_military'
        MILLENNIAL='etf_tags_millennial'
        MINERS='etf_tags_miners'
        MLP='etf_tags_mlp'
        MOBILE_PAYMENTS='etf_tags_mobilepayments'
        MODERATE='etf_tags_moderate'
        MOMENTUM='etf_tags_momentum'
        MONOPOLIES='etf_tags_monopolies'
        MSFT='etf_tags_msft'
        MULTI_ASSET='etf_tags_multiasset'
        MULTI_FACTOR='etf_tags_multifactor'
        MULTI_SECTOR='etf_tags_multisector'
        MUNICIPAL_BONDS='etf_tags_municipalbonds'
        MUSIC='etf_tags_music'
        NASDAQ_COMPOSITE='etf_tags_nasdaqcomposite'
        NASDAQ_ONE_HUNDRED='etf_tags_nasdaq100'
        NATURAL_GAS='etf_tags_naturalgas'
        NATURAL_RESOURCES='etf_tags_naturalresources'
        NETHERLANDS='etf_tags_netherlands'
        NETWORK='etf_tags_network'
        NEW_ZEALAND='etf_tags_newzealand'
        NEXT_GEN='etf_tags_nextgen'
        NFLX='etf_tags_nflx'
        NICKEL='etf_tags_nickel'
        NIGERIA='etf_tags_nigeria'
        NIKKEI_FOUR_HUNDRED='etf_tags_nikkei400'
        NON_ESG='etf_tags_nonesg'
        NORTH_AMERICA='etf_tags_northamerica'
        NORWAY='etf_tags_norway'
        NUCLEAR_ENERGY='etf_tags_nuclearenergy'
        NVDA='etf_tags_nvda'
        OCEAN='etf_tags_ocean'
        OIL='etf_tags_oil'
        OIL_GAS_EXP_PROD='etf_tags_oilgasexpprod'
        OIL_GAS_SERVICES='etf_tags_oilgasservices'
        ONLINE_STORES='etf_tags_onlinestores'
        OPTIONS='etf_tags_options'
        PAKISTAN='etf_tags_pakistan'
        PALLADIUM='etf_tags_palladium'
        PATENTS='etf_tags_patents'
        PERU='etf_tags_peru'
        PET_CARE='etf_tags_petcare'
        PHARMACEUTICAL='etf_tags_pharmaceutical'
        PHILIPPINES='etf_tags_philippines'
        PHYSICAL='etf_tags_physical'
        PIPELINES='etf_tags_pipelines'
        PLATINUM='etf_tags_platinum'
        POLAND='etf_tags_poland'
        POLITICS='etf_tags_politics'
        PORTUGAL='etf_tags_portugal'
        PRECIOUS_METALS='etf_tags_preciousmetals'
        PREFERRED='etf_tags_preferred'
        PREFERRED_SECURITIES='etf_tags_preferredsecurities'
        PRIVATE_CREDIT='etf_tags_privatecredit'
        PRIVATE_EQUITY='etf_tags_privateequity'
        PUT_WRITE='etf_tags_putwrite'
        PYPL='etf_tags_pypl'
        QUALITY='etf_tags_quality'
        QUANTITATIVE='etf_tags_quantitative'
        QUANTUM_COMPUTING='etf_tags_quantumcomputing'
        QUATAR='etf_tags_quatar'
        R_AND_D='etf_tags_rd'
        RARE_EARTH='etf_tags_rareearth'
        REAL_ASSETS='etf_tags_realassets'
        REAL_ESTATE='etf_tags_realestate'
        REGIONAL_BANKS='etf_tags_regionalbanks'
        REITS='etf_tags_reits'
        RELATIVE_STRENGTH='etf_tags_relativestrength'
        RENEWABLE_ENERGY='etf_tags_renewableenergy'
        REPUBLICANS='etf_tags_republicans'
        RESPONSIBLE='etf_tags_responsible'
        RESTAURANT='etf_tags_restaurant'
        RETAIL='etf_tags_retail'
        RETAIL_STORES='etf_tags_retailstores'
        REVENUE='etf_tags_revenue'
        RISING_RATES='etf_tags_risingrates'
        ROBOTICS='etf_tags_robotics'
        RUSSELL_ONE_THOUSAND='etf_tags_russell1000'
        RUSSELL_TWO_HUNDRED='etf_tags_russell200'
        RUSSELL_TWO_THOUSAND='etf_tags_russell2000'
        RUSSELL_TWO_THOUSAND_FIVE_HUNDRED='etf_tags_russell2500'
        RUSSELL_THREE_THOUSAND='etf_tags_russell3000'
        SAUDI_ARABIA='etf_tags_saudiarabia'
        SECTOR_ROTATION='etf_tags_sectorrotation'
        SEMICONDUCTORS='etf_tags_semiconductors'
        SENIOR_LOANS='etf_tags_seniorloans'
        SHARIA_COMPLIANT='etf_tags_shariacompliant'
        SHIPPING='etf_tags_shipping'
        SHORT='etf_tags_short'
        SILVER='etf_tags_silver'
        SILVER_MINERS='etf_tags_silverminers'
        SINGAPORE='etf_tags_singapore'
        SINGLE_ASSET='etf_tags_singleasset'
        SLV='etf_tags_slv'
        SMALL_CAP='etf_tags_smallcap'
        SMALL_MID_CAP='etf_tags_smallmidcap'
        SMART_GRID='etf_tags_smartgrid'
        SMART_MOBILITY='etf_tags_smartmobility'
        SOCIAL='etf_tags_social'
        SOCIAL_MEDIA='etf_tags_socialmedia'
        SOFTWARE='etf_tags_software'
        SOLAR='etf_tags_solar'
        SOUTH_AFRICA='etf_tags_southafrica'
        SOUTH_KOREA='etf_tags_southkorea'
        SOYBEAN='etf_tags_soybean'
        SP_ONE_HUNDRED='etf_tags_sp100'
        SP_ONE_THOUSAND='etf_tags_sp1000'
        SP_ONE_THOUSAND_FIVE_HUNDRED='etf_tags_sp1500'
        SP_FOUR_HUNDRED='etf_tags_sp400'
        SP_FIVE_HUNDRED='etf_tags_sp500'
        SP_SIX_HUNDRED='etf_tags_sp600'
        SPAC='etf_tags_spac'
        SPACE_EXPLORATION='etf_tags_spaceexploration'
        SPAIN='etf_tags_spain'
        SPIN_OFF='etf_tags_spinoff'
        STEEL='etf_tags_steel'
        SUGAR='etf_tags_sugar'
        SUKUK='etf_tags_sukuk'
        SUSTAINABILITY='etf_tags_sustainability'
        SWEDEN='etf_tags_sweden'
        SWITZERLAND='etf_tags_switzerland'
        TACTICAL='etf_tags_tactical'
        TAIWAN='etf_tags_taiwan'
        TARGET_DRAWDOWN='etf_tags_targetdrawdown'
        TECHNOLOGY='etf_tags_technology'
        THAILAND='etf_tags_thailand'
        TIMBER='etf_tags_timber'
        TIPS='etf_tags_tips'
        TRANSPORTATION='etf_tags_transportation'
        TRAVEL='etf_tags_travel'
        TREASURIES='etf_tags_treasuries'
        TSLA='etf_tags_tsla'
        TURKEY='etf_tags_turkey'
        U_K='etf_tags_uk'
        U_S='etf_tags_us'
        UAE='etf_tags_uae'
        UPSIDE_CAP='etf_tags_upsidecap'
        UPSTREAM='etf_tags_upstream'
        URANIUM='etf_tags_uranium'
        URANIUM_MINERS='etf_tags_uraniumminers'
        USD='etf_tags_usd'
        USO='etf_tags_uso'
        UTILITIES='etf_tags_utilities'
        VALUE='etf_tags_value'
        VARIABLE_RATE='etf_tags_variablerate'
        VEGAN='etf_tags_vegan'
        VIETNAM='etf_tags_vietnam'
        VIX='etf_tags_vix'
        VOLATILITY='etf_tags_volatility'
        VOLATILITY_INDEX='etf_tags_volatilityindex'
        VOLATILITY_WEIGHT='etf_tags_volatilityweight'
        WATER='etf_tags_water'
        WEAPONS='etf_tags_weapons'
        WELLNESS='etf_tags_wellness'
        WHEAT='etf_tags_wheat'
        WIND='etf_tags_wind'
        WOOD='etf_tags_wood'
        XOM='etf_tags_xom'
        YUAN='etf_tags_yuan'
        ZERO_COUPON='etf_tags_zerocoupon'

    def filter_tags(self, tags: Tags):
        self.filters['Tags'] = tags

    def get_params(self) -> dict:
        """
        Returns filter parameters in the format expected by FinViz.
        """
        params = {'f': ','.join(self.filters.values())}
        if self.manual_filters:
            params['f'] += ',' + ','.join(self.manual_filters)
        return params

    @classmethod
    def get_filter_ids(cls) -> list[str]:
        """
        Returns a list of available filter ids as strings.
        """
        return [
            'Exchange',
            'Index',
            'Sector',
            'Industry',
            'Country',
            'MarketCap',
            'PE',
            'ForwardPE',
            'Peg',
            'PS',
            'PB',
            'PriceCash',
            'PriceFreeCashFlow',
            'EpsGrowththisYear',
            'EpsGrowthnextYear',
            'EpsGrowthpastFiveYears',
            'EpsGrowthnextFiveYears',
            'SalesGrowthpastFiveYears',
            'EpsGrowthqtrOverQtr',
            'SalesGrowthqtrOverQtr',
            'EpsGrowthTtm',
            'SalesGrowthTtm',
            'EarningsAndRevenueSurprise',
            'DividendYield',
            'ReturnOnAssets',
            'ReturnOnEquity',
            'ReturnOnInvestedCapital',
            'CurrentRatio',
            'QuickRatio',
            'LtDebtEquity',
            'DebtEquity',
            'GrossMargin',
            'OperatingMargin',
            'NetProfitMargin',
            'PayoutRatio',
            'Insiderownership',
            'Insidertransactions',
            'Institutionalownership',
            'Institutionaltransactions',
            'ShortFloat',
            'AnalystRecom',
            'OptionShort',
            'EarningsDate',
            'Performance',
            'PerformanceTwo',
            'Volatility',
            'RsiFourteen',
            'Gap',
            'SimpleMovingAverage20Day',
            'SimpleMovingAverage50Day',
            'SimpleMovingAverage200Day',
            'Change',
            'ChangeFromOpen',
            'HighLow20Day',
            'HighLow50Day',
            'FiftyTwoWeekHighLow',
            'AllTimeHighLow',
            'Pattern',
            'Candlestick',
            'Beta',
            'AverageTrueRange',
            'AverageVolume',
            'RelativeVolume',
            'PriceDollar',
            'TargetPrice',
            'IpoDate',
            'SharesOutstanding',
            'Float',
            'LatestNews',
            'AssetType',
            'Sponsor',
            'NetExpenseRatio',
            'NetFundFlows',
            'AnnualizedReturn',
            'Tags',
        ]
