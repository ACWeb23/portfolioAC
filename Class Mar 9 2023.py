# Write your code here :-)
class Weapon:
    def __init__(self, x, y, z, angle, image, fireRate, punch, recoil, zoom = None):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.image = image
        self.fireRate = fireRate
        self.punch = punch
        self.recoil = recoil
        self.zoom = zoom

class kineticWeapon(Weapon):
    def __init__(self, x, y, z, angle, image, fireRate, punch, recoil, maxAmmo, currentAmmo, maxClip, currentClip, zoom = None):
        super().__init__( x, y, z, angle, image, fireRate, punch, recoil, zoom)


