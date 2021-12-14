#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : funcparserlib
Version  : 1.0.0a0
Release  : 34
URL      : https://github.com/vlasovskikh/funcparserlib/archive/refs/tags/1.0.0a0.tar.gz
Source0  : https://github.com/vlasovskikh/funcparserlib/archive/refs/tags/1.0.0a0.tar.gz
Summary  : Recursive descent parsing library based on functional combinators
Group    : Development/Tools
License  : MIT
Requires: funcparserlib-license = %{version}-%{release}
Requires: funcparserlib-python = %{version}-%{release}
Requires: funcparserlib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(poetry)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
funcparserlib
=============
Recursive descent parsing library for Python based on functional combinators.

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
%setup -q -n funcparserlib-1.0.0a0
cd %{_builddir}/funcparserlib-1.0.0a0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638822138
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/funcparserlib
cp %{_builddir}/funcparserlib-1.0.0a0/LICENSE %{buildroot}/usr/share/package-licenses/funcparserlib/9c43ed8af0243b23bbf87e137bfd753f4cc4b899
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/funcparserlib/9c43ed8af0243b23bbf87e137bfd753f4cc4b899

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
