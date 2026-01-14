#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Catalog
Summary:	XML::Catalog - Resolve public identifiers and remap system identifiers
Summary(pl.UTF-8):	XML::Catalog - rozwiązywanie identyfikatorów publicznych i przemapowywanie systemowych
Name:		perl-XML-Catalog
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c2c14f3e87aa75ebb7130ea4ebd41984
URL:		http://search.cpan.org/dist/XML-Catalog/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-URI
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements draft 0.4 of John Cowan's XML Catalog (formerly
known as XCatalog) proposal 
(<http://www.ccil.org/~cowan/XML/XCatalog.html>). Catalogs may be
written in either SOCAT or XML syntax (see the proposal for syntax
details); XML::Catalog will assume SOCAT syntax if the catalog is not
in well-formed XML syntax.

This module, as of 1.0.0, also supports Oasis XML catalogs.

%description -l pl.UTF-8
Ten moduł implementuje szkic (draft) wersji 0.4 propozycji XML Catalog
Johna Cowana (wcześniej znanej jako XCatalog:
<http://www.ccil.org/~cowan/XML/XCatalog.html>). Katalogi mogą być
pisane z użyciem składni SOCAT lub XML (szczegóły w propozycji;
XML::Catalog zakłada składnię SOCAT, jeśli katalog nie jest dobrze
sformułowanym XML-em).

Ten moduł w wersji 1.0.0 obsługuje także katalogi Oasis XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/Catalog.pm
%{_mandir}/man3/XML::Catalog.3pm*
