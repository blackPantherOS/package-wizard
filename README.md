# Package Wizard (DESTROYED)
# THIS REPO IT WAS OUR PACKAGE MANAGER SOURCE CODE!
# This loss thanks to Distrowatch.com because:
- the site does not want to display the correct valid information and released versions of small distros. For example: "Architecture: i586" at the bP is false.
- [Our BETA1](https://www.blackpantheros.eu/the-first-beta-release-of-blackpanther-os-v18-1-renegade/) it was announced as an new stable release on the DW, [the final](https://www.blackpantheros.eu/blackpanther-os-v18-1-renegade-released/) and [all previous or newer edition was not announced, not displayed on DW](https://hu-blackpanther-hu.translate.goog/tudasbazis/verzio-es-megjelenesek/?_x_tr_sl=hu&_x_tr_tl=en&_x_tr_hl=hu&_x_tr_pto=nui)
- does not check or moderate false allegations, for example this one from the site:

![ONE OF FAKE ALLEGATIONS](https://raw.githubusercontent.com/blackPantherOS/package-wizard/master/data/screenshots/fake.jpg)
 
# We don’t want to develop and support people who don’t respect the work of others.
# We reject any form of discrimination. We close this source and we will not open this code in the future,
# Our response to each destruction is to delete one of our source codes

Summary
---------
== English ==

A Qt5-based distribution-independent package manager and installer on PackageKit grounds. Its extra feature, in addition to a nice-looking interface, is its ability to install and manage Python Pip and Node Npm modules. 
This development is a modular part of the FusionLogic framework, a sub-project in the development of the blackPanther distribution.
It is free to use for everyone on the condition of displaying the authors site and observing the GPL3 rules.
It is a very simple and eye-catching application, simply click on an RPM or DEB package and install it using the systems PackageKit.

This application is a really easy-to-use piece of software. 
Just click and install any application (RPM,DEB) package on your favourite system.

Under development:
 - setting the image that can be seen in the pictures as well to fit the distribution as early as the setup phase
 - improving the look and feel
 - localising the missing strings
 - monitoring the use of other package manager applications, suspending the installation process
 - database preloader for faster startup

Awaiting implementation:
 - Managing NPM modules
 - Managing PIP modules
 - Uniform package list, installation of the package manager for batch package management
 - further integration and optional switching of packagekit-python
 - integration and optional switching of other package management engines
 - Any other request package format support

# (Screenshots bellow)

Installation
----------
on blackPanther OS, Hungarian distribution:
```
installing package-wizard
```


On other distributions from source:
```
cd /a/place/where/you/have/write/permission (or as root)
git clone --recurse-submodules https://github.com/blackPantherOS/package-wizard.git
cd package-wizard/fusionlogic-common
python3 setup.py build
# (you will have to run it as root)
python3 setup.py install

cd ..
python3 setup.py build
python3 setup.py install
```
Use:

Get the informations for usage
```
package-wizard --help
```

## Examples
Application installation from PackageKit package database, e.g. Gimp:
```
package-wizard --install gimp
```

Application Uninstallation from system, e.g. Gimp:
```
package-wizard --uninstall gimp
```

Installation from a local package: 
```
package-wizard --install /where/your/package/is/located/packagename.rpm(or deb)
```

*****************
Összefoglalás
---------
== Hungarian ==

Qt5 alapú disztrófüggetlen szoftvercsomag kezelő és telepítő PackageKit alapokon
Extra tulajdonsága egy csinos felületent túl, a Python Pip és Node Npm modulok telepítése, 
kezelése.  Ez a fejelsztés a FusionLogic® keretrendszer moduláriS része, ami egy alprojekt 
a blackPanther OS disztribúció fejlesztésében.

© Szabadon elérhető bárkinek a szerzői oldal megjelenítése mellett, és a GPL3 szabályok betartásával.

Ez egy nagyon egyszerű és látványos alkalmazás, csak kattints rá egy RPM, DEB csomagkra és
telepítsd a rendszer-PackageKit használatával.

Az alkalmazás egy roppant könnyen használható program.
Kattintson és telepítsen bármilyen alkalmazáscsomagot kedvenc rendszerére.

Fejlesztés alatt:
 - a képeken is látható arculat beállítása a disztribúciónak megfelelően már a setup szakaszban
 - arculat javítása
 - a kihagyott feliratok honosítása
 - más csomagkezelő alkalmazások használatának figyelése, telepítési folyamat felfüggesztése
 - adatbázis preloader a gyorsabb indításhoz
 
Megvalósításra vár
 - NPM modulok kezelése
 - PIP modulok kezelése
 - egységes csomaglista, csomagkezelő beépítése a kötegelt csomagkezlésekhez
 - packagekit-python tovébbi integrációja és opcionális váltása
 - egyéb csomagkezelő motorok integrációja és opcionális váltása
 - bármilyen más kért csomagformátum támogatása

Telepítés
----------
blackPanther OS magyar disztribúcióra:
```
telepites package-wizard
```

Forrásból más disztribúcióra:
```
cd /egy/hely/ahova/van/írási/jogod (vagy root joggal)
git clone --recurse-submodules https://github.com/blackPantherOS/package-wizard.git
cd package-wizard/fusionlogic-common
python3 setup.py build
# (ezt már root joggal kell futtatnod)
python3 setup.py install

cd ..
python3 setup.py build
python3 setup.py install

```
### Használat:

Egy program telepítés PackageKit csomagadatbázisból, például Gimp:
```
package-wizard --install gimp
```
Egy program eltávolítása, például a Gimp:

```
package-wizard --uninstall gimp
```


Telepítés egy helyi fájlból:
```
package-wizard --install /ahol/a/fájlod/van/csomagenve.rpm(vagy deb)
```

Screenshots
----------
![package-wizard-distros](https://raw.githubusercontent.com/blackPantherOS/package-wizard/master/data/screenshots/distro_variants.png)
![package-wizard-main](https://raw.githubusercontent.com/blackPantherOS/package-wizard/master/data/screenshots/screenshot-main.png)

******************
