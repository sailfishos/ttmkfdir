Summary: Utility to create fonts.scale files for truetype fonts
Name:    ttmkfdir
Version: 3.0.9
Release: 1
URL:     https://github.com/sailfishos/ttmkfdir.git 
Source0: %{name}-%{version}.tar.bz2

Patch:   ttmkfdir-3.0.9-cpp.patch
Patch1:  ttmkfdir-3.0.9-zlib.patch
Patch2:  ttmkfdir-3.0.9-fix-freetype217.patch
Patch3:  ttmkfdir-3.0.9-namespace.patch
Patch4:  ttmkfdir-3.0.9-fix-crash.patch
Patch5:  ttmkfdir-3.0.9-warnings.patch
Patch6:  ttmkfdir-3.0.9-segfaults.patch
Patch7:  ttmkfdir-3.0.9-encoding-dir.patch
Patch8:  ttmkfdir-3.0.9-font-scale.patch
Patch9:  ttmkfdir-3.0.9-bug434301.patch

# Only licensing attribution is in README, no version.
License: LGPLv2+

BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel flex
BuildRequires: libtool

# ttmkfdir used to be in the following packages at one point
Conflicts: XFree86-font-utils < 4.2.99.2-0.20021126.3
Conflicts: freetype < 2.0.6-3

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/ttmkfdir

