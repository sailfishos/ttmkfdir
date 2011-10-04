Summary: Utility to create fonts.scale files for truetype fonts
Name: ttmkfdir
Version: 3.0.9
Release: 32
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: %{name}-%{version}.tar.bz2
Patch: ttmkfdir-3.0.9-cpp.patch
Patch1: ttmkfdir-3.0.9-zlib.patch
Patch2: ttmkfdir-3.0.9-fix-freetype217.patch
Patch3: ttmkfdir-3.0.9-namespace.patch
Patch4: ttmkfdir-3.0.9-fix-crash.patch
Patch5: ttmkfdir-3.0.9-warnings.patch
Patch6: ttmkfdir-3.0.9-segfaults.patch
Patch7: ttmkfdir-3.0.9-encoding-dir.patch
Patch8: ttmkfdir-3.0.9-font-scale.patch
Patch9: ttmkfdir-3.0.9-bug434301.patch
# Only licensing attribution is in README, no version.
License: LGPLv2+
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/ttmkfdir

