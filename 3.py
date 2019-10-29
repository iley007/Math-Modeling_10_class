import const
from const import g
def fulll (m,h,v):
    """ фуккция определяет полную механническую энергию
        m - масса
        h- высота подброса
        v- скорость движения на высоте
    """
    E=m*g*h+(m*v**2)/2
    print(E, 'Дж')
    
fulll (50,200,3)
       