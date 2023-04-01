UsePaletteMode = 1
- can be used if images having <=255 colors.
- uses picture palette, in some cases could reduce pack weight.
- create file image.cfg with content 1,4,2,5,66 (near .json) to inverse image writing mode for selected image IDs
- will compress images if it's not fitting in 255 color palette
UsePaletteMode = 0
- can provide more quality for image.
- normally working with 24&16bit images, raw look. Can greatly increase the size of the build.


v2.1.6
- Preview bugfixes
- Watchfaces generating with random header identifier
- Fixed problem with Windows scaling, DPI is tied to 96
- [WFPreview] Removed ability to clone watchface header

v2.1.5
- Preview bugfixes
- [WFPreview] Added Copy/Paste/Save ability
- [WFPreview] Added ability to clone watchface header

v2.1.4
- Pandafix (new unknown element)
- BugFixe

v2.0.0
- Mi Band 5 Watchface support
- raw.cfg changed to image.cfg
- added new parameter "UsePaletteMode" to WatchFace.exe.config
- swithed to 24 bit pixel color

Use it with full understanding that it can cause problems with Mi band 5 device, use it at your own risk.