# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['your_script_name.py'],
    pathex=[],
    binaries=[],
    datas=[('riotgames.pem', '.'), ('./riot/champ-theme/Jinx/get-jinxed-1.mp3', './riot/champ-theme/Jinx'), ('./riot/champ-theme/Jinx/get-jinxed-2.mp3', './riot/champ-theme/Jinx'), ('./riot/champ-theme/Jinx/get-jinxed-3.mp3', './riot/champ-theme/Jinx'), ('./riot/champ-theme/Jinx/get-jinxed-4.mp3', './riot/champ-theme/Jinx'), ('./riot/champ-theme/Jinx/get-jinxed-5.mp3', './riot/champ-theme/Jinx')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='your_script_name',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
