#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Trigram
Summary:	String::Trigram - find similar strings by trigram method
Summary(pl.UTF-8):	String::Trigram - poszukiwanie podobnych łańcuchów metodą trygramów
Name:		perl-String-Trigram
Version:	0.11
Release:	10
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43e5234ecfb00ab06f5f07f45043b6dc
URL:		http://search.cpan.org/dist/String-Trigram/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module computes the similarity of two strings based on the
trigram method. This consists in splitting some string into triples of
characters and comparing those to the trigrams of some other string.
For example the string kangaroo has the trigrams {kan ang nga gar aro
roo}. A wrongly typed kanagaroo has the trigrams {kan ana nag aga gar
aro roo}. To compute the similarity we (roughly) divide the number of
matching trigrams (tokens not types) by the number of all trigrams
(types not tokens). For our example this means dividing 4 / 9
resulting in 0.44.

%description -l pl.UTF-8
Ten moduł oblicza podobieństwo dwóch łańcuchów bazując na metodzie
trygramów. Składa się ona z dzielenia łańcucha na trójki znaków i
porównywanie tych trygramów z jakimś innym łańcuchem. Na przykład
łańcuch "kangaroo" zawiera trygramy {kan ang nga gar aro roo}. Źle
napisane "kanagaroo" zawiera trygramy {kan ana nag aga gar aro roo}.
Aby obliczyć podobieństwo, dzielimy (zgrubnie) liczbę pasujących
trygramów (tokenów, nie typów) przez liczbę wszystkich trygramów
(typów, nie tokenów). W naszym przykładzie oznacza to dzielenie 4 / 9,
co daje wartość 0.44.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/String/*.pm
%dir %{perl_vendorarch}/auto/String/Trigram
%attr(755,root,root) %{perl_vendorarch}/auto/String/Trigram/*.so
%{_mandir}/man3/*
