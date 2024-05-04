print('''
                            _
                                   .-.  .--''` )
                                _ |  |/`   .-'`
                               ( `\      /`
                               _)   _.  -'._
                             /`  .'     .-.-;
                             `).'      /  \  \
                            (`,        \_o/_o/__
                             /           .-''`  ``'-.
                             {         /` ,___.--''`
                             {   ;     '-. \ \
           _   _             {   |'-....-`'.\_\
          / './ '.           \   \          `"`
       _  \   \  |            \   \
      ( '-.J     \_..----.._ __)   `\--..__
     .-`                    `        `\    ''--...--.
    (_,.--""`/`         .-             `\       .__ _)
            |          (                 }    .__ _)
            \_,         '.               }_  - _.'
               \_,         '.            } `'--'
                  '._.     ,_)          /
                     |    /           .'
                      \   |    _   .-'
                       \__/;--.||-'
                        _||   _||__   __
                 _ __.-` "`)(` `"  ```._)
           jgs  (_`,-   ,-'  `''-.   '-._)
               (  (    /          '.__.'
                `"`'--'

''')
print("Welcome Welcome hahaha!!! to Tresureeee Island  the land of Dreams come true \n ")

print("Your quest being now your choice us your key \n")

print("Challenge 1 HAHAHAHAHAHAHA")
road =  input( " Choose a part Do you want to go left or right? \n")
if road.upper() == "LEFT":
    print("You are now on your quest")
    print("challenge 2  hint in every action there is a rection ")
    action = input("You found food and you are very hungry should you eat or pass : \n")

    if action.upper() == "EAT":
        print("No matter the problem chop first ")
        print("final quest  hint risk is your friend ")

        risk = input("You found unidentified black scary box  open, don't touch , pass \n ")

        if risk.upper() == "OPEN":
            print("You win  never judge a book by it cover ")
        else:
            print("Fear is fake  Game over ")
    else:
        print("Game over ")
   
else:
    print("Game over try again")

