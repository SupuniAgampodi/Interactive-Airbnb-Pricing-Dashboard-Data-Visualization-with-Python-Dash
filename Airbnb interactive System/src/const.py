def get_constants(df):
    total_listings = len(df)
    neighbourhood_count = df['neighbourhood_cleansed'].nunique()
    property_type_count = df['property_type'].nunique()
    room_type_count = df['room_type'].nunique()

    return total_listings, neighbourhood_count, property_type_count, room_type_count
