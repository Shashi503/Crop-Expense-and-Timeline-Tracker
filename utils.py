CROPS = [
    'Arecanut', 'Other Kharif pulses', 'Rice', 'Banana', 'Cashewnut', 'Coconut', 
    'Dry ginger', 'Sugarcane', 'Sweet potato', 'Tapioca', 'Black pepper', 
    'Dry chillies', 'other oilseeds', 'Turmeric', 'Maize', 'Moong(Green Gram)', 
    'Urad', 'Arhar/Tur', 'Groundnut', 'Sunflower', 'Bajra', 'Castor seed', 
    'Cotton(lint)', 'Horse-gram', 'Jowar', 'Korra', 'Ragi', 'Tobacco', 'Gram', 
    'Wheat', 'Masoor', 'Sesamum', 'Linseed', 'Safflower', 'Onion', 
    'other misc. pulses', 'Samai', 'Small millets', 'Coriander', 'Potato', 
    'Other  Rabi pulses', 'Soyabean', 'Beans & Mutter(Vegetable)', 'Bhindi', 
    'Brinjal', 'Citrus Fruit', 'Cucumber', 'Grapes', 'Mango', 'Orange', 
    'other fibres', 'Other Fresh Fruits', 'Other Vegetables', 'Papaya', 
    'Pome Fruit', 'Tomato', 'Rapeseed &Mustard', 'Mesta', 'Cowpea(Lobia)', 
    'Lemon', 'Pome Granet', 'Sapota', 'Cabbage', 'Peas  (vegetable)', 'Niger seed', 
    'Bottle Gourd', 'Sannhamp', 'Varagu', 'Garlic', 'Ginger', 'Oilseeds total', 
    'Pulses total', 'Jute', 'Peas & beans (Pulses)', 'Blackgram', 'Paddy', 
    'Pineapple', 'Barley', 'Khesari', 'Guar seed', 'Moth', 'Other Cereals & Millets', 
    'Cond-spcs other', 'Turnip', 'Carrot', 'Redish', 'Arcanut (Processed)', 
    'Atcanut (Raw)', 'Cashewnut Processed', 'Cashewnut Raw', 'Cardamom', 'Rubber', 
    'Bitter Gourd', 'Drum Stick', 'Jack Fruit', 'Snak Guard', 'Pump Kin', 'Tea', 
    'Coffee', 'Cauliflower', 'Other Citrus Fruit', 'Water Melon', 'Total foodgrain', 
    'Kapas', 'Colocosia', 'Lentil', 'Bean', 'Jobster', 'Perilla', 'Rajmash Kholar', 
    'Ricebean (nagadal)', 'Ash Gourd', 'Beet Root', 'Lab-Lab', 'Ribed Guard', 'Yam', 
    'Apple', 'Peach', 'Pear', 'Plums', 'Litchi', 'Ber', 'Other Dry Fruit', 'Jute & mesta'
]

ACTIVITY_CATEGORIES = {
    '🧪 Pre-Sowing / Land Prep': ['Land clearing', 'Ploughing / Tilling', 'Soil testing', 'Land leveling', 'Bed preparation', 'Organic matter application (manure/compost)'],
    '🌱 Sowing / Planting': ['Seed purchase', 'Sowing / Planting labor', 'Nursery preparation', 'Seed treatment'],
    '💧 Irrigation': ['Irrigation labor', 'Electricity/diesel for pump', 'Pipe / drip maintenance', 'Water tank charges (if bought)'],
    '🐛 Crop Protection': ['Pesticide purchase', 'Pesticide spraying labor', 'Fungicide/Herbicide purchase', 'Traps (e.g., pheromone/sticky)'],
    '🪴 Crop Nutrition': ['Fertilizer purchase', 'Fertilizer application labor', 'Organic fertilizer/compost/bio-enzyme'],
    '✂️ Crop Maintenance': ['Weeding', 'Pruning', 'Support structures (bamboo, wires, ropes)', 'Mulching'],
    '🚜 Harvesting': ['Harvest labor', 'Bags/containers/crates', 'Sorting & Grading', 'Temporary storage'],
    '🚚 Post-Harvest / Marketing': ['Transport to mandi', 'Loading/unloading charges', 'Market fees/commission', 'Packaging materials'],
    '🔩 Tools & Equipment': ['Purchase (sprayer, sickle, hoe, etc.)', 'Repairs & maintenance', 'Fuel & lubricants'],
    '👷 Labour Wages': ['Permanent labor', 'Daily wage workers', 'Seasonal contracts'],
    '📋 Other / Miscellaneous': ['Government fees', 'Agri consultancy', 'Mobile recharge (for agri apps)', 'Electricity bill', 'Others']
}