#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : funcparserlib
Version  : 0.3.6
Release  : 22
URL      : https://files.pythonhosted.org/packages/cb/f7/b4a59c3ccf67c0082546eaeb454da1a6610e924d2e7a2a21f337ecae7b40/funcparserlib-0.3.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/f7/b4a59c3ccf67c0082546eaeb454da1a6610e924d2e7a2a21f337ecae7b40/funcparserlib-0.3.6.tar.gz
Summary  : Recursive descent parsing library based on functional combinators
Group    : Development/Tools
License  : MIT
Requires: funcparserlib-license = %{version}-%{release}
Requires: funcparserlib-python = %{version}-%{release}
Requires: funcparserlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
funcparserlib
=============
A recurisve descent parsing library based on functional combinators.

%package license
Summary: license components for the funcparserlib package.
Group: Default

%description license
license components for the funcparserlib package.


%package python
Summary: python components for the funcparserlib package.
Group: Default
Requires: funcparserlib-python3 = %{version}-%{release}

%description python
python components for the funcparserlib package.


%package python3
Summary: python3 components for the funcparserlib package.
Group: Default
Requires: python3-core
Provides: pypi(funcparserlib)

%description python3
python3 components for the funcparserlib package.


%prep
%setup -q -n funcparserlib-0.3.6
cd %{_builddir}/funcparserlib-0.3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603392188
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/funcparserlib
cp %{_builddir}/funcparserlib-0.3.6/LICENSE %{buildroot}/usr/share/package-licenses/funcparserlib/479411487eedf488118f11a6563c94e13be645b3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/funcparserlib/479411487eedf488118f11a6563c94e13be645b3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
