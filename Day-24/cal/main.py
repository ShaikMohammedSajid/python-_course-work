"""
import logic

logic.add(2,3)
logic.sub(3,4)
logic.mul(3,4)
logic.div(2,3)
logic.rem(2,3)
logic.exp(2,3)

# module as asliyasnames as we wanted name we use aliyasname :
# instead of using logic we can write a name lg or anything

import logic as lg

lg.add(2,3)
lg.sub(3,4)
lg.mul(3,4)
lg.div(2,3)
lg.rem(2,3)
lg.exp(3,4)

#IF WE WANT IMPORT A PARTICULAR TOPIC WE CAN DO IT LIKE THIS:
from logic import add,sub
add(2,3)
sub(3,4)
"""

# IF WE WANT TO ALL OF THEM WITHOUT FILE NAME WE CAN DO LIKE THIS:

from logic import *
add(23,2)
sub(3,4)
mul(3,4)
div(2,3)
rem(2,3)
exp(3,4)