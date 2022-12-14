# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['scripts\\compress_geotiff.py'],
    pathex=[],
    binaries=[],
    datas=[('.\\venv\\Lib\\site-packages\\rasterio\\proj_data', 'rasterio\\proj_data')],
    hiddenimports=['rasterio.sample', 'rasterio.vrt','rasterio._features'],
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
    name='compress_geotiff',
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
