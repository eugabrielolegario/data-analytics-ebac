from haversine import haversine
import matplotlib.pyplot as plt


los_angeles = (-15.848929, -48.116189)
toquio = (-15.838145, -48.054989)

#function to calculate the distance in lat and lng between 2 points
def cal_lat_lng(lat_a, lng_a, lat_b,lng_b):
    point1= (lat_a, lng_a)
    point2= (lat_b, lng_b)

    
    return round(haversine(point1, point2, unit='km'), 2)



#function to change image size
def my_figsize(height, width):
    fig,ax = plt.subplots(figsize=(height, width))