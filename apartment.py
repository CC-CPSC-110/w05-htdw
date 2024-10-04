"""Apartment example."""
import math
from typing import List
from dataclasses import dataclass
from typing_extensions import Self
from cs110 import expect, summarize


@dataclass
class Apartment:
    """A class to describe an apartment."""
    address: str
    price: int
    latitude: float   #  -90 to  90
    longitude: float  # -180 to 180

    def distance(self, apt: Self) -> float:
        """
        Purpose: Gets the distance between this and another apartment.
        Examples:
            apartments = [
                    Apartment(
                        latitude = 49.28268912323915, 
                        longitude = -123.13115296063464
                        ...
                    ),
                    Apartment(
                        latitude = 49.27736281422789, 
                        longitude = -123.12668440036572
                        ...
                    ),
                    Apartment(
                        latitude = 49.27352901325701, 
                        longitude = -123.12602017298748
                        ...
                    )
                ]
            apartments[0].distance(apartments[0]) -> 0
            apartments[0].distance(apartments[1]) -> 0.00695
            apartments[0].distance(apartments[2]) -> 0.01050

        """
        distance_lat = self.latitude - apt.latitude
        distance_lon = self.longitude - apt.longitude
        return math.sqrt(distance_lat ** 2 + distance_lon ** 2)
                


    def closest(self, loa: List[Self]) -> Self | None:
        """
        Purpose: Returns the closest apartment to this one.
        Examples:
            apartments = [
                Apartment(
                    latitude = 49.28268912323915, 
                    longitude = -123.13115296063464
                    ...
                ),
                Apartment(
                    latitude = 49.27736281422789, 
                    longitude = -123.12668440036572
                    ...
                ),
                Apartment(
                    latitude = 49.27352901325701, 
                    longitude = -123.12602017298748
                    ...
                )
            ]
            apartments[0].closest(apartments) -> None
            apartments[1].closest(apartments) -> apartments[2]

        """
        close: Self | None = None
        for apartment in loa:
            # Skip if it's the same apartment as the reference
            if apartment == self:
                continue

            if close is None:
                close = apartment

            else:
                distance_cls_lat = self.latitude - close.latitude
                distance_cls_lon = self.longitude - close.longitude
                distance_cls = math.sqrt(distance_cls_lat ** 2 + distance_cls_lon ** 2)

                distance_apt_lat = self.latitude - apartment.latitude
                distance_apt_lon = self.longitude - apartment.longitude
                distance_apt = math.sqrt(distance_apt_lat ** 2 + distance_apt_lon ** 2)
                
                if distance_apt < distance_cls:
                    close = apartment
        return close
    
    
    def set_price(self, price: int):
        self.price = price



# The database is a list of apartments
# The data is real data from Google Maps
apartments = [
    Apartment(
        address = "1104-1157 Jepson-Young Ln, Vancouver, BC, Canada",
        price = 2050,
        latitude = 49.28268912323915, 
        longitude = -123.13115296063464
    ),
    Apartment(
        address = "718 Davie St, Vancouver, BC, Canada",
        price = 3050,
        latitude = 49.27736281422789, 
        longitude = -123.12668440036572
    ),
    Apartment(
        address = "1399 Homer St, Vancouver, BC, Canada",
        price = 2875,
        latitude = 49.27352901325701, 
        longitude = -123.12602017298748
    )
]

my_apt = Apartment(
        address = "1104-1157 Jepson-Young Ln, Vancouver, BC, Canada",
        price = 2050,
        latitude = 49.28268912323915, 
        longitude = -123.13115296063464
)

expect(my_apt.distance(apartments[0]),       0, tolerance=0.0001)
expect(my_apt.distance(apartments[1]), 0.00695, tolerance=0.0001)
expect(my_apt.distance(apartments[2]), 0.01050, tolerance=0.0001)

expect(my_apt.closest(apartments), apartments[1])
expect(apartments[1].closest(apartments), apartments[2])
summarize()