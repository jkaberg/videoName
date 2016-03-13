videoName
---

An simple tool to match an renamed media file (based on a hash value) against Opensubtitles database.

Nice to have if you renamed a few movies/series and want to rollback to the original filename.

# Usage
---
```
/path/to/script.py -user *username* -pass *password* -p /path/to/media/file.mkv
```


# Example output
---
```
FileName: Runner.Runner.2013.720p.AVC.AC3-IDK
Path: /path/to/media/Runner.Runner.2013.720p.AVC.AC3-IDK/Runner.Runner.2013.720p.AVC.AC3-IDK.mkv

|   Score | Name                                               |
|---------+----------------------------------------------------|
|      74 | Runner.Runner.2013.720p.WEB-DL.H264-HD             |
|      73 | Runner.Runner.2013.720p.WEB-DL.H264-PHD            |
|      70 | Runner.Runner.2013.720p.WEB-DL.H264-PublicHD       |
|      69 | Runner.Runner.2013.720p.BluRay.x264.YIFY           |
|      68 | Runner.Runner.2013.720p.WEB-DL.H264-PublicHD       |
|      68 | Runner.Runner.2013.720p.BluRay.x264-SPARKS         |
|      68 | Runner.Runner.2013.1080p-720p.BrRip.x264-YIFY      |
|      66 | Runner.Runner.2013.HDRip.XviD-AQOS                 |
|      64 | Runner.Runner.2013.SLO.BluRay.720p.x264.DTS-HDWinG |
|      64 | Runner.Runner.2013.DVDRip.x264-SPARKS              |
|      64 | Runner Runner 2013 720p WEB-DL x264 AC3-JYK        |
|      63 | Runner.Runner.2013.HDRip.X264-PLAYNOW              |
|      62 | Runner.Runner.2013.1080p.BluRay.x264.SPARKS        |
|      61 | Runner.Runner.2013.HDRip.X264-PLAYNOW-spa          |
|      61 | Runner.Runner.2013.HDRip.X264-PLAYNOW-hi           |
|      61 | Runner.Runner.2013.HDRip.X264-PLAYNOW              |
|      60 | Runner Runner 2013                                 |
|      58 | Runner.Runner.2013.1080p.BluRay.x264-SPARKS-.SRB   |
|      58 | Runner Runner (2013)                               |
|      57 | Runner Runner 2013 BRRip XviD AC3-SANTi            |
|      56 | Runner Runner 2013 720p WEB-DL H264-PublicHD       |
|      56 | Runner Runner 2013 720p BluRay DTS x264-PHD        |
|      53 | Runner Runner 2013 HDRip XviD-TST                  |
|      53 | Runner Runner 2013 HDRip XviD-SaM                  |
|      53 | Runner Runner 2013 CAM V2 x264 AAC-MiLLENiUM       |
|      50 | Runner Runner [2013]HDRip XviD-SaM[ETRG]           |
|      50 | Runner Runner 2013 HDRip X264-PLAYNOW              |
|      48 | Runner_Runner_[2013]HDRip_XviD-SaM[ETRG]           |
|      44 | Runner Runner [2013]HDRip XviD-SaM[ETRG]-cze(1)    |

```