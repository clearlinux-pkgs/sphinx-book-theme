#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinx-book-theme
Version  : 0.1.7
Release  : 6
URL      : https://files.pythonhosted.org/packages/2b/8c/50526eac2d3520e8b17d21faeafbbd7d42dba682b44770fd00fa401ce829/sphinx-book-theme-0.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/8c/50526eac2d3520e8b17d21faeafbbd7d42dba682b44770fd00fa401ce829/sphinx-book-theme-0.1.7.tar.gz
Summary  : Jupyter Book: Create an online book with Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sphinx-book-theme-license = %{version}-%{release}
Requires: sphinx-book-theme-python = %{version}-%{release}
Requires: sphinx-book-theme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(click)
BuildRequires : pypi(docutils)
BuildRequires : pypi(importlib_resources)
BuildRequires : pypi(pydata_sphinx_theme)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(sphinx)

%description
[![codecov][codecov-badge]][codecov-link] [![Documentation Status][rtd-badge]][rtd-link] [![PyPI][pypi-badge]][pypi-link]
        
        **An interactive book theme for Sphinx**.
        
        This is a lightweight Sphinx theme designed to mimic the look-and-feel of an

%package license
Summary: license components for the sphinx-book-theme package.
Group: Default

%description license
license components for the sphinx-book-theme package.


%package python
Summary: python components for the sphinx-book-theme package.
Group: Default
Requires: sphinx-book-theme-python3 = %{version}-%{release}

%description python
python components for the sphinx-book-theme package.


%package python3
Summary: python3 components for the sphinx-book-theme package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_book_theme)
Requires: pypi(beautifulsoup4)
Requires: pypi(click)
Requires: pypi(docutils)
Requires: pypi(importlib_resources)
Requires: pypi(pydata_sphinx_theme)
Requires: pypi(pyyaml)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinx-book-theme package.


%prep
%setup -q -n sphinx-book-theme-0.1.7
cd %{_builddir}/sphinx-book-theme-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637596896
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . click
pypi-dep-fix.py . docutils
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx-book-theme
cp %{_builddir}/sphinx-book-theme-0.1.7/LICENSE %{buildroot}/usr/share/package-licenses/sphinx-book-theme/99ca545faafef4ff35bee85e9485dce69e2bca54
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} click
pypi-dep-fix.py %{buildroot} docutils
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx-book-theme/99ca545faafef4ff35bee85e9485dce69e2bca54

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
