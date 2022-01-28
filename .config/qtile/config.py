from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile import bar, layout, widget, qtile, hook
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from custom.layouts import Max, MaxFocus, MonadFocus
from custom.widgets import CPU

from os.path import expanduser
import subprocess


M4 = 'mod4'
M1 = 'mod1'

keys = [
    # Move window focus
    Key([M4], "h", lazy.layout.left()),
    Key([M4], "l", lazy.layout.right()),
    Key([M4], "j", lazy.layout.down()),
    Key([M4], "k", lazy.layout.up()),
    Key([M4], "space", lazy.layout.next()),

    # Move the window
    Key([M4, "shift"], "h", lazy.layout.shuffle_left()),
    Key([M4, "shift"], "l", lazy.layout.shuffle_right()),
    Key([M4, "shift"], "j", lazy.layout.shuffle_down()),
    Key([M4, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize the Windows
    Key([M4], 'u', lazy.layout.shrink()),
    Key([M4], 'i', lazy.layout.grow()),
    Key([M4], "o", lazy.layout.maximize()),
    Key([M4], "y", lazy.layout.normalize()),

    # Print ( date +  clipboard yank )
    Key([M4], 'p', lazy.spawn('./scripts/print.sh')),
    Key([M4, 'shift' ], 'p', lazy.spawn('./scripts/print_select.sh')),

    # Functions
    Key([M4], "q", lazy.window.kill()),
    Key([M4], "e", lazy.hide_show_bar()),
    Key([M4], 'r', lazy.spawncmd()),
    # Move to layout
    KeyChord([M4], 'w', [
        Key([], '1', lazy.to_layout_index(index=0)),
        Key([], '2', lazy.to_layout_index(index=1)),
        Key([], '3', lazy.to_layout_index(index=2)),
        Key([], '4', lazy.to_layout_index(index=3)),
        ]),

    # Apps
    Key([M1], '1', lazy.spawn("kitty --single-instance")),
    Key([M1], '2', lazy.spawn("emacsclient -c -a 'emacs'")),
    Key([M1], '3', lazy.spawn('librewolf')),
    Key([M1], '4', lazy.spawn('nautilus')),
    Key([M1], '5', lazy.spawn('gimp')),
    Key([M1], '6', lazy.spawn('spotify')),
    Key([M1], '7', lazy.spawn('discord')),

    # Volume
    Key([M1], 'q', lazy.spawn('amixer -q -D pulse set Master 10%-')),
    Key([M1], 'w', lazy.spawn('amixer -q -D pulse set Master 10%+')),
    Key([M1], 'e', lazy.spawn('amixer -q -D pulse set Master toggle')),

    # Scripts
    Key([M1], 'h', lazy.spawn('sudo ./scripts/clear_drop_caches.sh')),

    # Qtile Managemant
    Key([M1, 'control'], '1', lazy.restart()),
    Key([M1, 'control'], '2', lazy.shutdown()),

    # Session
    Key([M1, 'control'], '3', lazy.spawn('shutdown now')),
    Key([M1, 'control'], '4', lazy.spawn('reboot')),
]

groups = [
    Group(name=n, label=l)

    if n not in ['s', 'x']

    else

    Group(name=n, label=l, layout='monadfocus')

    for n, l in [('a', '\ufa9e'),
                 ('s', '\ue7c5'),
                 ('d', '\uf489'),
                 ('f', '\uf233'),
                 ('g', '\uf1d7'),
                 ('z', '\uf1bc'),
                 ('x', '\uf11b'),
                 ('c', '\uf108'),
                 ('v', '\ue5ff'),
                 ('b', '\ue28c')]
    ]

for i in groups:
    keys.extend([
        # Switch to a group
        Key([M4], i.name, lazy.group[i.name].toscreen()),

        # Move focused to a group
        Key([M4, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False)),
    ])

palette = ['#5b00a4',
           '#528ff1',
           '#5c2ecb',
           '#5c2ecb',
           '#5c2ecb',
           '#5c2ecb',
           '#5c2ecb',
           '#d7c6e3']

monad_options = {
    'border_width': 3,
    'margin': 5,
    'border_focus': palette[0],
    'border_normal': palette[1],
    'align': 1,
    'max_ratio': 0.7,
    'min_ratio': 0.3,
    'change_ratio': 0.02,
    'min_secondary_size': 245
}

max_options = {
    'margin': 5,
    'border_width': 2,
    'border_focus': palette[1]
}

layouts = [
    Monad(**monad_options),
    MonadFocus(**monad_options),
    Max(**max_options),
    MaxFocus(**max_options),
    layout.Floating(border_focus = palette[0],
                    border_normal = palette[1]
    )
]

floating_layout = layouts[4]

widget_defaults = dict(
    font='FiraCode',
    fontsize=14,
    padding=1,
)

extension_defaults = widget_defaults.copy()

textbox = {'fontsize': '20',
           'padding': 0}

top_bar = bar.Bar(
    size=20,
    opacity=1,
    margin=[5, 5, 0, 5],
    widgets = [
        widget.TextBox(
            text=" ",
            **textbox,
            background=palette[1]
            ),

        widget.Image(
            filename='~/ahaha.png',
            background=palette[1]
            ),

        widget.Prompt(
            background=palette[1],
            foreground='#000000',
            prompt=' >_ '
            ),

        widget.TextBox(
            text="\uE0B0\uE0B1",
            font='FiraCode Bold',
            **textbox,
            background=palette[0],
            foreground=palette[1]
            ),

        widget.GroupBox(
            highlight_method='line',
            font='FiraCode Bold',
            fontsize=25,
            margin=3,
            highlight_color=[palette[0], palette[0]],
            this_current_screen_border=palette[1],
            urgent_alert_method=palette[2],
            inactive=palette[7],
            active=palette[1],
            background=palette[0],
            ),

        widget.TextBox(
            text="\uE0B0",
            **textbox,
            background=palette[2],
            foreground=palette[0]
            ),

        widget.WindowName(
            padding=10,
            empty_group_string='hireki@nano',
            background=palette[2],
            foreground=palette[7]
            ),

        widget.TextBox(
            text="\uE0B2",
            **textbox,
            background=palette[2],
            foreground=palette[1]
            ),

        widget.Image(
            margin=2,
            filename='~/cpu.png',
            background=palette[1]
            ),

        CPU(
            format=' ({freq_current}Ghz) {load_percent}%',
            background=palette[1],
            foreground=palette[3]
            ),

        widget.Image(
            margin=2,
            filename='~/thermometer.png',
            background=palette[1]
            ),

        widget.ThermalSensor(
            fmt='{}  ',
            background=palette[1],
            foreground=palette[3]),

        widget.TextBox(
            text=" ",
            font='FiraCode Bold',
            **textbox,
            background=palette[1],
            foreground=palette[2]
            ),

        widget.Image(
            filename='~/ram.png',
            background=palette[1]
            ),

        widget.Memory(
            format=" {MemFree: .0f}M ",
            measure_mem="M",
            background=palette[1],
            foreground=palette[4]
            ),

        widget.TextBox(
            text="",
            font='FiraCode Bold',
            **textbox,
            background=palette[1],
            foreground=palette[2]
            ),

        widget.Image(
            margin=2,
            filename='~/graphics-card.png',
            background=palette[1]
            ),

        widget.NvidiaSensors(
            format="{temp}°C",
            padding=10,
            background=palette[1],
            foreground=palette[5]
            ),

        widget.TextBox(
            text="",
            font='FiraCode Bold',
            **textbox,
            background=palette[1],
            foreground=palette[2]
            ),

        widget.Image(
            margin=2,
            filename='~/loud-speaker.png',
            background=palette[1]
            ),

        widget.PulseVolume(
            fmt='{}',
            padding=10,
            background=palette[1],
            foreground=palette[6]
            ),

        widget.TextBox(
            text="\uE0B3\uE0B2",
            font='FiraCode Bold',
            **textbox,
            background=palette[1],
            foreground=palette[2]
            ),

        widget.Systray(background=palette[2]),

        widget.Clock(
            padding=10,
            format='%a %d %b %I:%M %p',
            background=palette[2],
            foreground=palette[7])
        ])

main_screen = Screen(
    top_bar,
    wallpaper_mode='fill',
    wallpaper='~/Pictures/wallpapers/Pixiv.Id.40752740.full.3503032.jpg',
)
screens = [main_screen]

mouse = [
    Drag([M4], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([M4], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([M4], "Button2", lazy.window.bring_to_front())
]

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False
auto_minimize = True
wmname = "LG3D"

@hook.subscribe.layout_change
def hide_bar_focus_layout(layout, group):
    """ Hide bar when in some focus layout """
    if group.screen: # avoid problems with screen start time
        bar = group.screen.top.is_show()
        if 'focus' in layout.name and bar is True:
            group.screen.top.show(False)
        elif bar is False:
            group.screen.top.show(True)

@hook.subscribe.startup_once
def start_once():
    subprocess.call([expanduser('~/') + '.config/qtile/autostart.sh'])
