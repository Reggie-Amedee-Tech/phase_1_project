def processMtaRidershipData(data: dict):
    mta_ridership_data = []
    for mta_data in data:
        mta_ridership_data.append({
            "date": mta_data["date"],
            "subways_total_estimated_ridership": mta_data["subways_total_estimated_ridership"],
            "subways_of_comparable_pre_pandemic_day": mta_data["subways_of_comparable_pre_pandemic_day"],
            "buses_total_estimated_ridersip": mta_data["buses_total_estimated_ridersip"],
            "buses_of_comparable_pre_pandemic_day": mta_data["buses_of_comparable_pre_pandemic_day"],
            "lirr_total_estimated_ridership": mta_data["lirr_total_estimated_ridership"],
            "lirr_of_comparable_pre_pandemic_day": mta_data["lirr_of_comparable_pre_pandemic_day"],
            "metro_north_total_estimated_ridership": mta_data["metro_north_total_estimated_ridership"],
            "metro_north_of_comparable_pre_pandemic_day": mta_data["metro_north_of_comparable_pre_pandemic_day"],
            "access_a_ride_total_scheduled_trips": mta_data["access_a_ride_total_scheduled_trips"],
            "access_a_ride_of_comparable_pre_pandemic_day": mta_data["access_a_ride_of_comparable_pre_pandemic_day"],
            "bridges_and_tunnels_total_traffic": mta_data["bridges_and_tunnels_total_traffic"],
            "bridges_and_tunnels_of_comparable_pre_pandemic_day": mta_data["bridges_and_tunnels_of_comparable_pre_pandemic_day"],
            "staten_island_railway_total_estimated_ridership": mta_data["staten_island_railway_total_estimated_ridership"],
            "staten_island_railway_of_comparable_pre_pandemic_day": mta_data["staten_island_railway_of_comparable_pre_pandemic_day"]
        })

    return mta_ridership_data