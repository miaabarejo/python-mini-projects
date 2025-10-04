print('Welcome to the Treasure Island.'
      'Your mission is to find the treasure.'
      'You\'re at a cross road. Where do you want to go?') #ahhh isang hilera parin siya na walang putol, para lang readable here
direction = input("Type left or right\n")
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('Type "wait"" to wait for a boat. Type "swim" to swim across.\n')
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color = input("One red, one yellow, and one blue. Which colour do you choose?\n")
        if color == "red":
            print("It's a room full of fire. Game over.")
        elif color == "yellow":
            print("You win")
        elif color == "blue":
            print("Eaten by the beasts. Game over.")
    elif wait_or_swim == "swim":
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole.\nGame over")

print('''
       899X7                                                X8997
     g999999Wm_                                         ,gm999999W.
   gW99*~~~~VM9Ws                                     ,m99*~~~~VM99m.
  g999`       '*99i                                  W9Af        Y99W.
  999[          '*9W_                             ,g9Af           999b
  999W            '*9W.                          g9Af            i9999
  9999W_            'V9W.       \.    ./       g9A~            ,g99999
  99999**Nm__          ~MW_.     N.  .N     _g9f`         ,_gm**M99999
  9999|   89999mms___    ~MWm.    [ ]`    gm9f`   ,___mmW9999|   8999P
  99999mmW99A***M9999999mms2M9s_,g+=Ye.,_W95_mmW9999999****999mmW9999[
  999999999`     '9999Af`  ~VM999P    9999*~`  ~*9999P      Y99999999[
  M9999AM99s.   ,g9999`       '99[    99P        Y999W_    _W99*99999!
  ]9999b'*999999999999b       _999.  d99b.      ,999999999999Af,99999
  'M9999i 'V*9999999999Wm__gmW9999[  99999mm__gm9999999999A*~  W9999f
    M9999s      ~~~~~~~~~~~~LmW99f   'M99ms7~~~~~~~~~~~`     ,W9999!
     V9999Ws_        ___mmW99999[      999999mms__.       ,_m9999A`
      '~*999999999999A**f~   ]9A[      A99   '~***999999999999Af~
          2999A*~~`          d9 9     ][]9.          ~~V*999K.
       ,gW9A~             ,_W9! 9[    9[ M9s_             'V99m_
      i999A            ,_W99f` i9[    9W  ~M99s_            !999W
      !9999ms_______mW99Af`   d99A.  /999.   ~*999ms_______mW999A
       Y9999f~~~~~~~~~`     gW9f~ +_z`'~M9m.     ~~~~~~~~~~M9999`
        V999            ,gm9Af`          ~*9Wm_            ]99A`
          ~*Nm______mmW99Af                 '*999mms_____gm*f`
             99999999                              99999999
''')