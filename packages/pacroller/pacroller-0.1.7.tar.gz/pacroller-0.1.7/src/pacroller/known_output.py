from pacroller.config import KNOWN_OUTPUT_OVERRIDE
KNOWN_HOOK_OUTPUT_OVERRIDE, KNOWN_PACKAGE_OUTPUT_OVERRIDE = KNOWN_OUTPUT_OVERRIDE

KNOWN_HOOK_OUTPUT = {
    '': [],
    '20-systemd-sysusers.hook': [
        r'(?i)creating group .+',
        r'(?i)creating user .+',
    ],
    '30-systemd-sysctl.hook': [
        r'Not setting (.+) \(explicit setting exists\)\.',
    ],
    '30-systemd-udev-reload.hook': [
        r'[ ][ ]Skipped: Device manager is not running\.',
    ],
    '90-mkinitcpio-install.hook': [
        r'==> Building image from preset: .+',
        r'==> Starting build: .+',
        r'==> WARNING: Possibly missing firmware for module: .+',
        r'==> Generating module dependencies',
        r'==> Creating (?:.+)-compressed initcpio image: .+',
        r'==> Image generation successful.*',
        r'[ ]+-> .+',
        r'ssh-.* .*',
    ],
    '70-dkms-upgrade.hook': [
        r'==> dkms remove --no-depmod -m .* -v .* -k .*',
    ],
    '70-dkms-install.hook': [
        r'==> dkms install --no-depmod -m .* -v .* -k .*',
        r'==> depmod .*',
    ],
    **KNOWN_HOOK_OUTPUT_OVERRIDE
}

_keyring_output = [
    r'==> Appending keys from .+',
    r'==> Locally signing trusted keys in keyring\.\.\.',
    r'==> Importing owner trust values\.\.\.',
    r'==> Disabling revoked keys in keyring\.\.\.',
    r'==> Updating trust database\.\.\.',
    r'gpg: next trustdb check due at .+',
    r'gpg: public key .+ is .+ than the signature',
    r'gpg: Warning: using insecure memory!',
    r'gpg: checking the trustdb',
    r'gpg: setting ownertrust to .+',
    r'gpg: marginals needed:.+ completes needed:.+ trust model: pgp',
    r'gpg: depth:.+ valid:.+ signed:.+ trust:.+, .+, .+, .+, .+, .+',
    r'gpg: key .+: no user ID for key signature packet of class .+',
    r'gpg: inserting ownertrust of .+',
    r'[ ]+-> .+',
]

_vbox_output = [
    r'0%\.\.\.10%\.\.\.20%\.\.\.30%\.\.\.40%\.\.\.50%\.\.\.60%\.\.\.70%\.\.\.80%\.\.\.90%\.\.\.100%',
]

KNOWN_PACKAGE_OUTPUT = {
    '': [],
    'archlinux-keyring': _keyring_output,
    'archlinuxcn-keyring': _keyring_output,
    'brltty': [
        r'Please add your user to the brlapi group\.',
    ],
    'glibc': [
        r'Generating locales\.\.\.',
        r'Generation complete\.',
        r'  .*_.*\.\.\. done',
    ],
    'fontconfig': [
        r'Rebuilding fontconfig cache\.\.\.',
    ],
    'nvidia-utils': [
        r'If you run into trouble with CUDA not being available, run nvidia-modprobe first\.',
    ],
    'virtualbox': _vbox_output,
    'virtualbox-ext-oracle': _vbox_output,
    'virtualbox-ext-vnc': _vbox_output,
    'virtualbox-ext-vnc-svn': _vbox_output,
    'tor-browser': [
        r'$',
        r'==> The copy of Tor Browser in your home directory will be upgraded at the',
        r'==> first time you run it as your normal user\. Just start it and have fun!',
    ],
    **KNOWN_PACKAGE_OUTPUT_OVERRIDE
}
