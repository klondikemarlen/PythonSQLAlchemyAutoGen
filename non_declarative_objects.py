########## Test object.
"""
Example of object to generate schema for as seen at
https://stackoverflow.com/questions/41201536/how-can-i-autogenerate-sqlalchemy-schema-from-non-declarative-objects/41924737#41924737

"""

class Order(object):
    """ generated source for class Order """

    #  main order fields
    m_orderId = 0
    m_clientId = 0
    m_permId = 0
    m_action = ""
    m_totalQuantity = 0
    m_orderType = ""
    m_lmtPrice = float()
    m_auxPrice = float()

    #  extended order fields
    m_tif = ""  #  "Time in Force" - DAY, GTC, etc.
    m_activeStartTime = ""  #  GTC orders
    m_activeStopTime = ""  #  GTC orders
    m_ocaGroup = "" #  one cancels all group name
    m_ocaType = 0   #  1 = CANCEL_WITH_BLOCK, 2 = REDUCE_WITH_BLOCK, 3 = REDUCE_NON_BLOCK
    m_orderRef = ""
    m_transmit = bool() #  if false, order will be created but not transmited
    m_parentId = 0  #  Parent order Id, to associate Auto STP or TRAIL orders with the original order.
    m_blockOrder = bool()
    m_sweepToFill = bool()
    m_displaySize = 0
    m_triggerMethod = 0 #  0=Default, 1=Double_Bid_Ask, 2=Last, 3=Double_Last, 4=Bid_Ask, 7=Last_or_Bid_Ask, 8=Mid-point
    m_outsideRth = bool()
    m_hidden = bool()
    m_goodAfterTime = ""    #  FORMAT: 20060505 08:00:00 {time zone}
    m_goodTillDate = ""     #  FORMAT: 20060505 08:00:00 {time zone}
    m_overridePercentageConstraints = bool()
    m_rule80A = ""  #  Individual = 'I', Agency = 'A', AgentOtherMember = 'W', IndividualPTIA = 'J', AgencyPTIA = 'U', AgentOtherMemberPTIA = 'M', IndividualPT = 'K', AgencyPT = 'Y', AgentOtherMemberPT = 'N'
    m_allOrNone = bool()
    m_minQty = 0
    m_percentOffset = float()   #  REL orders only; specify the decimal, e.g. .04 not 4
    m_trailStopPrice = float()  #  for TRAILLIMIT orders only
    m_trailingPercent = float()  #  specify the percentage, e.g. 3, not .03

    #  Financial advisors only 
    m_faGroup = ""
    m_faProfile = ""
    m_faMethod = ""
    m_faPercentage = ""

    #  Institutional orders only
    m_openClose = ""            #  O=Open, C=Close
    m_origin = 0                #  0=Customer, 1=Firm
    m_shortSaleSlot = 0         #  1 if you hold the shares, 2 if they will be delivered from elsewhere.  Only for Action="SSHORT
    m_designatedLocation = ""   #  set when slot=2 only.
    m_exemptCode = 0

    #  SMART routing only
    m_discretionaryAmt = float()
    m_eTradeOnly = bool()
    m_firmQuoteOnly = bool()
    m_nbboPriceCap = float()
    m_optOutSmartRouting = bool()

    #  BOX or VOL ORDERS ONLY
    m_auctionStrategy = 0   #  1=AUCTION_MATCH, 2=AUCTION_IMPROVEMENT, 3=AUCTION_TRANSPARENT


    #  BOX ORDERS ONLY
    m_startingPrice = float()
    m_stockRefPrice = float()
    m_delta = float()

    #  pegged to stock or VOL orders
    m_stockRangeLower = float()
    m_stockRangeUpper = float()

    #  VOLATILITY ORDERS ONLY
    m_volatility = float()  #  enter percentage not decimal, e.g. 2 not .02
    m_volatilityType = 0        #  1=daily, 2=annual
    m_continuousUpdate = 0
    m_referencePriceType = 0    #  1=Bid/Ask midpoint, 2 = BidOrAsk
    m_deltaNeutralOrderType = ""
    m_deltaNeutralAuxPrice = float()
    m_deltaNeutralConId = 0
    m_deltaNeutralSettlingFirm = ""
    m_deltaNeutralClearingAccount = ""
    m_deltaNeutralClearingIntent = ""
    m_deltaNeutralOpenClose = ""
    m_deltaNeutralShortSale = bool()
    m_deltaNeutralShortSaleSlot = 0
    m_deltaNeutralDesignatedLocation = ""

    #  COMBO ORDERS ONLY
    m_basisPoints = float() #  EFP orders only, download only
    m_basisPointsType = 0   #  EFP orders only, download only

    #  SCALE ORDERS ONLY
    m_scaleInitLevelSize = 0
    m_scaleSubsLevelSize = 0
    m_scalePriceIncrement = float()
    m_scalePriceAdjustValue = float()
    m_scalePriceAdjustInterval = 0
    m_scaleProfitOffset = float()
    m_scaleAutoReset = bool()
    m_scaleInitPosition = 0
    m_scaleInitFillQty = 0
    m_scaleRandomPercent = bool()
    m_scaleTable = ""

    #  HEDGE ORDERS ONLY
    m_hedgeType = ""    #  'D' - delta, 'B' - beta, 'F' - FX, 'P' - pair
    m_hedgeParam = ""   #  beta value for beta hedge (in range 0-1), ratio for pair hedge

    #  Clearing info
    m_account = ""          #  IB account
    m_settlingFirm = ""
    m_clearingAccount = ""  #  True beneficiary of the order
    m_clearingIntent = ""   #  "" (Default), "IB", "Away", "PTA" (PostTrade)

    #  ALGO ORDERS ONLY
    m_algoStrategy = ""
    m_algoParams = None

    #  What-if
    m_whatIf = bool()

    #  Not Held
    m_notHeld = bool()

    #  Smart combo routing params
    m_smartComboRoutingParams = None

    #  order combo legs
    m_orderComboLegs = []

    def __init__(self):
        """ generated source for method __init__ """
        self.m_lmtPrice = Double.MAX_VALUE
        self.m_auxPrice = Double.MAX_VALUE
        self.m_activeStartTime = self.EMPTY_STR
        self.m_activeStopTime = self.EMPTY_STR
        self.m_outsideRth = False
        self.m_openClose = "O"
        self.m_origin = self.CUSTOMER
        self.m_transmit = True
        self.m_designatedLocation = self.EMPTY_STR
        self.m_exemptCode = -1
        self.m_minQty = Integer.MAX_VALUE
        self.m_percentOffset = Double.MAX_VALUE
        self.m_nbboPriceCap = Double.MAX_VALUE
        self.m_optOutSmartRouting = False
        self.m_startingPrice = Double.MAX_VALUE
        self.m_stockRefPrice = Double.MAX_VALUE
        self.m_delta = Double.MAX_VALUE
        self.m_stockRangeLower = Double.MAX_VALUE
        self.m_stockRangeUpper = Double.MAX_VALUE
        self.m_volatility = Double.MAX_VALUE
        self.m_volatilityType = Integer.MAX_VALUE
        self.m_deltaNeutralOrderType = self.EMPTY_STR
        self.m_deltaNeutralAuxPrice = Double.MAX_VALUE
        self.m_deltaNeutralConId = 0
        self.m_deltaNeutralSettlingFirm = self.EMPTY_STR
        self.m_deltaNeutralClearingAccount = self.EMPTY_STR
        self.m_deltaNeutralClearingIntent = self.EMPTY_STR
        self.m_deltaNeutralOpenClose = self.EMPTY_STR
        self.m_deltaNeutralShortSale = False
        self.m_deltaNeutralShortSaleSlot = 0
        self.m_deltaNeutralDesignatedLocation = self.EMPTY_STR
        self.m_referencePriceType = Integer.MAX_VALUE
        self.m_trailStopPrice = Double.MAX_VALUE
        self.m_trailingPercent = Double.MAX_VALUE
        self.m_basisPoints = Double.MAX_VALUE
        self.m_basisPointsType = Integer.MAX_VALUE
        self.m_scaleInitLevelSize = Integer.MAX_VALUE
        self.m_scaleSubsLevelSize = Integer.MAX_VALUE
        self.m_scalePriceIncrement = Double.MAX_VALUE
        self.m_scalePriceAdjustValue = Double.MAX_VALUE
        self.m_scalePriceAdjustInterval = Integer.MAX_VALUE
        self.m_scaleProfitOffset = Double.MAX_VALUE
        self.m_scaleAutoReset = False
        self.m_scaleInitPosition = Integer.MAX_VALUE
        self.m_scaleInitFillQty = Integer.MAX_VALUE
        self.m_scaleRandomPercent = False
        self.m_scaleTable = self.EMPTY_STR
        self.m_whatIf = False
        self.m_notHeld = False
        
        
class Hero(object):
    class_attribute = 0
    
    def __init__(self, user_id=0):
        """Make a new Hero object.
        NOTE: user_id of zero is nobody ever. The minimum user_id is 1. :)
        """
        self.user_id = user_id
        self.name = "Admin"
        self.age = 7
        self.archetype = "Woodsman"
        self.specialization = "Hunter"
        self.religion = "Dryarch"
        self.house = "Unknown"
        self.current_exp = 0
        self.max_exp = 10
        self.renown = 0
        self.virtue = 0
        self.devotion = 0
        self.gold = 50

        self.ability_points = 3 #TEMP. Soon will use the 4 values below
        self.basic_ability_points = 0
        self.archetype_ability_points = 0
        self.specialization_ability_points = 0
        self.pantheonic_ability_points = 0

        self.attribute_points = 0
        self.primary_attributes = {"Strength": 1, "Resilience": 1, "Vitality": 1, "Fortitude": 1, "Reflexes": 1, "Agility": 1, "Perception": 1, "Wisdom": 1, "Divinity": 1, "Charisma": 1, "Survivalism": 1, "Fortuity": 1}
        self.current_sanctity = 0
        self.current_health = 0
        self.current_endurance = 0
        self.current_carrying_capacity = 0
        self.max_health = 0
		
        self.equipped_items = []
        self.inventory = []
        self.abilities = []
        self.chest_equipped = []

        self.errands = []
        self.current_quests = []
        self.completed_quests = []
        self.completed_achievements = []
        self.kill_quests = {}
        self.bestiary = []

        self.known_locations = []
        self.current_world = None
        self.current_city = None
        
        self.wolf_kills = 0


    def __str__(self):
        """Return string representation of Hero opject.
        """
        
        data = "Character object with attributes:"
        atts = []
        for key in sorted(vars(self).keys()):
            atts.append('{}: {} -> type: {}'.format(key, repr(vars(self)[key]), type(vars(self)[key])))
        data = '\n'.join(atts)
        return data
 
        
    def get_primary_attributes(self):
        return sorted(self.primary_attributes.items())        