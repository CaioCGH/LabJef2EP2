create or replace function t_validate_travel_request (state json)

returns json as
$body$
    import time

    plpy.info('inside t_validate_travel_request')    
    #time.sleep(30)
    
    plpy.info(state)
    return '{"customer_status": "Validated", "hotel_status": "Requested", "air_ticket_status": "Requested", "car_status": "Requested", "order_status": "Validated"}'
$body$
language plpython3u;

create or replace function t_buy_air_ticket (state json)
returns json as
$body$
    import time

    plpy.info('inside t_buy_air_ticket')    
    #time.sleep(30)
    
    plpy.info(state)

    return '{"air_ticket_status": "Purchased"}'
$body$
language plpython3u;

create or replace function t_reserve_hotel (state json)
returns json as
$body$
    import time

    plpy.info('inside t_reserve_hotel')    
    #time.sleep(30)
    
    plpy.info(state)

    return '{"hotel_status": "Reserved"}'
$body$
language plpython3u;

create or replace function t_reserve_car (state json)
returns json as
$body$
    import time

    plpy.info('inside t_reserve_car')    
    #time.sleep(30)
    
    plpy.info(state)

    return '{"car_status": "Reserved"}'
$body$
language plpython3u;

create or replace function t_close_travel_request (state json)
returns json as
$body$
    import time

    plpy.info('inside t_close_travel_request')    
    #time.sleep(30)
    
    plpy.info(state)

    return '{"order_status": "Finalized"}'
$body$
language plpython3u;


