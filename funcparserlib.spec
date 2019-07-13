#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : funcparserlib
Version  : 0.3.6
Release  : 13
URL      : https://files.pythonhosted.org/packages/cb/f7/b4a59c3ccf67c0082546eaeb454da1a6610e924d2e7a2a21f337ecae7b40/funcparserlib-0.3.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/f7/b4a59c3ccf67c0082546eaeb454da1a6610e924d2e7a2a21f337ecae7b40/funcparserlib-0.3.6.tar.gz
Summary  : Recursive descent parsing library based on functional combinators
Group    : Development/Tools
License  : MIT
Requires: funcparserlib-python3
Requires: funcparserlib-license
Requires: funcparserlib-python
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
Requires: funcparserlib-python3

%description python
python components for the funcparserlib package.


%package python3
Summary: python3 components for the funcparserlib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the funcparserlib package.


%prep
%setup -q -n funcparserlib-0.3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536550475
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/funcparserlib
cp LICENSE %{buildroot}/usr/share/doc/funcparserlib/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/funcparserlib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
