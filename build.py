# -*- coding: utf-8 -*-

from pathlib import Path
import xml.etree.ElementTree as xml
import hashlib
import shutil

TMP_DIR = 'tmp'
SOURCE_DIR = 'source'
REPO_DIR = 'repository'
ADDON_XML = 'addon.xml'
COMMON_XML = 'addons.xml'


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# CREATE *.ZIP FILES
xmlList = Path('./').glob('**/%s' % ADDON_XML)
for addonXml in xmlList:
    srcDir = './{0}'.format('/'.join(addonXml._parts[:-1]))
    tempDir = './{0}'.format(TMP_DIR)
    addonVersion = xml.parse(str(addonXml)).getroot().attrib['version']
    addonName = xml.parse(str(addonXml)).getroot().attrib['id']
    addonFile = '{0}-{1}'.format(addonName, addonVersion)
    zipPath = './{0}/{1}/{2}.zip'.format(REPO_DIR, addonName, addonFile)
    md5Path = './{0}/{1}/{2}.md5'.format(REPO_DIR, addonName, addonFile)
    shutil.rmtree(tempDir, ignore_errors=True)
    if not Path(zipPath).exists():
        shutil.copytree(srcDir, tempDir + '/' + addonName)
        shutil.make_archive(zipPath.replace('.zip', ''), 'zip', tempDir)
        shutil.rmtree(tempDir, ignore_errors=True)

# CREATE COMMON ADDONS.XML
xmlList = Path('./').glob('**/%s' % ADDON_XML)
common_xml = './{0}/{1}'.format(REPO_DIR, COMMON_XML)
with open(common_xml, 'wb') as outfile:
    outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
    outfile.write('<addons>')
    for addonXml in xmlList:
        with open('./' + str(addonXml), 'rb') as infile:
            for line in infile:
                if '<?xml' not in line:
                    outfile.write(line)
    outfile.write('</addons>')
    outfile.close()

# CREATE COMMON ADDONS.XML.MD5
common_md5 = md5(common_xml)
with open(common_xml + '.md5', 'wb') as hash_file:
    hash_file.write(common_md5)
