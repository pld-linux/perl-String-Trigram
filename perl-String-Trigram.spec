#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Trigram
Summary:	String::Trigram - find similar strings by trigram method
Summary(pl):	String::Trigram - poszukiwanie podobnych ³añcychów metod± trygramów
Name:		perl-String-Trigram
Version:	0.1
Release:	2
Epoch:		1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9a3fa223aec21df075ba4a065c60e57
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten modu³ oblicza podobieñstwo dwóch ³añcuchów bazuj±c na metodzie
trygramów. Sk³ada siê ona z dzielenia ³añcucha na trójki znaków i
porównywanie tych trygramów z jakim¶ innym ³añcuchem. Na przyk³ad
³añcuch "kangaroo" zawiera trygramy {kan ang nga gar aro roo}. ¬le
napisane "kanagaroo" zawiera trygramy {kan ana nag aga gar aro roo}.
Aby obliczyæ podobieñstwo, dzielimy (zgrubnie) liczbê pasuj±cych
trygramów (tokenów, nie typów) przez liczbê wszystkich trygramów
(typów, nie tokenów). W naszym przyk³adzie oznacza to dzielenie 4 / 9,
co daje warto¶æ 0.44.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/String/*.pm
%dir %{perl_vendorarch}/auto/String/Trigram
%{perl_vendorarch}/auto/String/Trigram/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/String/Trigram/*.so
%{_mandir}/man3/*
