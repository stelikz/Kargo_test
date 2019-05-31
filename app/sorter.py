# SORTER FOR JOBS
# ORIGIN
# ASC
def partition_jobs_by_origin_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].origin.lower()

    for j in range(low, high):

        if arr[j].origin.lower() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_origin_asc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_origin_asc(arr, low, high)

        quickSort_jobs_by_origin_asc(arr, low, pi - 1)
        quickSort_jobs_by_origin_asc(arr, pi + 1, high)

# DESC
def partition_jobs_by_origin_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].origin.lower()

    for j in range(low, high):

        if arr[j].origin.lower() >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_origin_desc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_origin_desc(arr, low, high)

        quickSort_jobs_by_origin_desc(arr, low, pi - 1)
        quickSort_jobs_by_origin_desc(arr, pi + 1, high)

# DESTINATION
# ASC
def partition_jobs_by_destination_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].destination.lower() 

    for j in range(low, high):

        if arr[j].destination.lower() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_destination_asc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_destination_asc(arr, low, high)

        quickSort_jobs_by_destination_asc(arr, low, pi - 1)
        quickSort_jobs_by_destination_asc(arr, pi + 1, high)

# DESC
def partition_jobs_by_destination_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].destination.lower()

    for j in range(low, high):

        if arr[j].destination.lower() >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_jobs_by_destination_desc(arr, low, high):
    if low < high:
   
        pi = partition_jobs_by_destination_desc(arr, low, high)

        quickSort_jobs_by_destination_desc(arr, low, pi - 1)
        quickSort_jobs_by_destination_desc(arr, pi + 1, high)

# BUDGET
# ASC
def partition_jobs_by_budget_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].budget 

    for j in range(low, high):

        if arr[j].budget <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_budget_asc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_budget_asc(arr, low, high)

        quickSort_jobs_by_budget_asc(arr, low, pi - 1)
        quickSort_jobs_by_budget_asc(arr, pi + 1, high)

# DESC
def partition_jobs_by_budget_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].budget

    for j in range(low, high):

        if arr[j].budget >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_jobs_by_budget_desc(arr, low, high):
    if low < high:
   
        pi = partition_jobs_by_budget_desc(arr, low, high)

        quickSort_jobs_by_budget_desc(arr, low, pi - 1)
        quickSort_jobs_by_budget_desc(arr, pi + 1, high)


# SHIPMENT DATE
# ASC
def partition_jobs_by_shipment_date_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].shipment_date 

    for j in range(low, high):

        if arr[j].shipment_date <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_shipment_date_asc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_shipment_date_asc(arr, low, high)

        quickSort_jobs_by_shipment_date_asc(arr, low, pi - 1)
        quickSort_jobs_by_shipment_date_asc(arr, pi + 1, high)

# DESC
def partition_jobs_by_shipment_date_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].shipment_date

    for j in range(low, high):

        if arr[j].shipment_date >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_jobs_by_shipment_date_desc(arr, low, high):
    if low < high:
   
        pi = partition_jobs_by_shipment_date_desc(arr, low, high)

        quickSort_jobs_by_shipment_date_desc(arr, low, pi - 1)
        quickSort_jobs_by_shipment_date_desc(arr, pi + 1, high)

# DISTANCE
# ASC
def partition_jobs_by_distance_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].distance 

    for j in range(low, high):

        if arr[j].distance <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_jobs_by_distance_asc(arr, low, high):
    if low < high:
        pi = partition_jobs_by_distance_asc(arr, low, high)

        quickSort_jobs_by_distance_asc(arr, low, pi - 1)
        quickSort_jobs_by_distance_asc(arr, pi + 1, high)

# DESC
def partition_jobs_by_distance_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].distance

    for j in range(low, high):

        if arr[j].distance >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_jobs_by_distance_desc(arr, low, high):
    if low < high:
   
        pi = partition_jobs_by_distance_desc(arr, low, high)

        quickSort_jobs_by_distance_desc(arr, low, pi - 1)
        quickSort_jobs_by_distance_desc(arr, pi + 1, high)


# SORTER FOR BIDS
# TRANSPORTER_NAME
# ASC
def partition_bids_by_transporter_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].transporter_name.lower()

    for j in range(low, high):

        if arr[j].transporter_name.lower() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_bids_by_transporter_asc(arr, low, high):
    if low < high:
        pi = partition_bids_by_transporter_asc(arr, low, high)

        quickSort_bids_by_transporter_asc(arr, low, pi - 1)
        quickSort_bids_by_transporter_asc(arr, pi + 1, high)

# DESC
def partition_bids_by_transporter_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].transporter_name.lower()

    for j in range(low, high):

        if arr[j].transporter_name.lower() >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_bids_by_transporter_desc(arr, low, high):
    if low < high:
   
        pi = partition_bids_by_transporter_desc(arr, low, high)

        quickSort_bids_by_transporter_desc(arr, low, pi - 1)
        quickSort_bids_by_transporter_desc(arr, pi + 1, high)

# TRANSPORTER_RATING
# ASC
def partition_bids_by_rating_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].transporter_rating 

    for j in range(low, high):

        if arr[j].transporter_rating <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_bids_by_rating_asc(arr, low, high):
    if low < high:
        pi = partition_bids_by_rating_asc(arr, low, high)

        quickSort_bids_by_rating_asc(arr, low, pi - 1)
        quickSort_bids_by_rating_asc(arr, pi + 1, high)

# DESC
def partition_bids_by_rating_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].transporter_rating

    for j in range(low, high):

        if arr[j].transporter_rating >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_bids_by_rating_desc(arr, low, high):
    if low < high:
   
        pi = partition_bids_by_rating_desc(arr, low, high)

        quickSort_bids_by_rating_desc(arr, low, pi - 1)
        quickSort_bids_by_rating_desc(arr, pi + 1, high)

# PRICE
# ASC
def partition_bids_by_price_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].price 

    for j in range(low, high):

        if arr[j].price <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_bids_by_price_asc(arr, low, high):
    if low < high:
        pi = partition_bids_by_price_asc(arr, low, high)

        quickSort_bids_by_price_asc(arr, low, pi - 1)
        quickSort_bids_by_price_asc(arr, pi + 1, high)

# DESC
def partition_bids_by_price_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].price

    for j in range(low, high):

        if arr[j].price >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_bids_by_price_desc(arr, low, high):
    if low < high:
   
        pi = partition_bids_by_price_desc(arr, low, high)

        quickSort_bids_by_price_desc(arr, low, pi - 1)
        quickSort_bids_by_price_desc(arr, pi + 1, high)

# VEHICLE_NAME
# ASC
def partition_bids_by_vehicle_asc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].vehicle_name.lower() 

    for j in range(low, high):

        if arr[j].vehicle_name.lower() <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort_bids_by_vehicle_asc(arr, low, high):
    if low < high:
        pi = partition_bids_by_vehicle_asc(arr, low, high)

        quickSort_bids_by_vehicle_asc(arr, low, pi - 1)
        quickSort_bids_by_vehicle_asc(arr, pi + 1, high)

# DESC
def partition_bids_by_vehicle_desc(arr, low, high):
    i = (low - 1)
    pivot = arr[high].vehicle_name.lower()

    for j in range(low, high):

        if arr[j].vehicle_name.lower() >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort_bids_by_vehicle_desc(arr, low, high):
    if low < high:
   
        pi = partition_bids_by_vehicle_desc(arr, low, high)

        quickSort_bids_by_vehicle_desc(arr, low, pi - 1)
        quickSort_bids_by_vehicle_desc(arr, pi + 1, high)
