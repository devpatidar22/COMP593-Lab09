from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox
# Create the window
root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(width=FALSE,height=FALSE)

# Add Frames to window
# Top
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20, 10))
#Bottom Left
frm_btm_left = ttk.LabelFrame(root, text="Info")
frm_btm_left.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)
#Bottom Right
frm_btm_right = ttk.LabelFrame(root, text="Stats")
frm_btm_right.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky=N)

# Add widgets to window

# Top ------> Pokemen Name
lbl_name = ttk.Label(frm_top, text='Pokémon Name:')
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    #pokemon name from user
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return
    
    #pokemon information according to name
    poke_info = get_pokemon_info(poke_name)
   
    if poke_info is None:
        err_msg = f'Unable to fetch information for {poke_name.capitalize()} from the POKEAPI.'
        messagebox.showinfo(title='Error', message = err_msg, icon = 'error')
        return
    # Bottom Left ------> Info 
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    lbl_weight_value['text'] = f"{poke_info['weight']} hg"
    lbl_type_value['text'] = poke_info['types'][0]['type']['name'].capitalize()
    i = len(poke_info['types'])
    for x in range(1,i):
        lbl_type_value['text'] = lbl_type_value['text'] + ", " + poke_info['types'][x]['type']['name'].capitalize()
    
    # Bottom Right ------> Stats
    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defense['value'] = poke_info['stats'][2]['base_stat']
    bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_special_defense['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']
       
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

# Bottom Left ------> Info
#Height
lbl_height= ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx = (10,5), pady = (10,5), sticky=E)

lbl_height_value= ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1, padx = (0,10), pady = (10,5), sticky=W)

#Weight
lbl_weight= ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx = (10,5), pady = (10,5), sticky=E)

lbl_weight_value= ttk.Label(frm_btm_left, text='TBD')
lbl_weight_value.grid(row=1, column=1, padx = (0,10), pady = (10,5), sticky=W)

#Type
lbl_type= ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx = (10,5), pady = (10,5), sticky=E)

lbl_type_value= ttk.Label(frm_btm_left, text='TBD')
lbl_type_value.grid(row=2, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Bottom Right ------> Stats
# HP
lbl_hp= ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Attack
lbl_attack= ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Defense
lbl_defense= ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Special Attack
lbl_special_attack= ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_attack.grid(row=3, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Special Defense
lbl_special_defense= ttk.Label(frm_btm_right, text='Special Defense:')
lbl_special_defense.grid(row=4, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_special_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_defense.grid(row=4, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Speed
lbl_speed= ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, padx = (10,5), pady = (10,5), sticky=E)

bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1, padx = (0,10), pady = (10,5), sticky=W)

# Loop until window is closed
root.mainloop()