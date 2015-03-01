#
# Conditional build:
%bcond_without	opt		# build opt

%define		main_ver	4.02.1
%define		subver		1

%define		doc_ver		3.06

%ifarch x32
%undefine	with_opt
%endif

%define		module	camlp4
Summary:	Objective Caml Preprocessor
Summary(pl.UTF-8):	Preprocesor OCamla
Name:		ocaml-camlp4
Version:	%{main_ver}.%{subver}
Release:	2
Epoch:		1
License:	LGPL v2 with linking exception
Group:		Libraries
Source0:	https://github.com/ocaml/camlp4/archive/%{main_ver}+%{subver}/camlp4-%{version}.tar.gz
# Source0-md5:	8c19bcca52b92a5496dcbcbb931a988b
# following 4 URLs are dead, some version now available at http://pauillac.inria.fr/camlp4/
Source1:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{doc_ver}-manual.html.tar.gz
# Source1-md5:	21370bae4e7f6435b38aeb21db7ce8bb
Source2:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{doc_ver}-manual.dvi.gz
# Source2-md5:	035915d1a530aa7ec9b194d9a7d258eb
Source3:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{doc_ver}-tutorial.html.tar.gz
# Source3-md5:	96d8eb4ca5abd58c9a280ba59f73b192
Source4:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{doc_ver}-tutorial.dvi.gz
# Source4-md5:	fcd87c235109364242a0c9ccf176dff8
URL:		https://github.com/ocaml/camlp4
BuildRequires:	ocaml >= 1:4.02
%requires_eq	ocaml-runtime
Provides:	camlp4 = %{epoch}:%{version}-%{release}
Obsoletes:	camlp4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

Camlp4 can parse normal Ocaml concrete syntax or any other
user-definable syntax. As an example, an alternative syntax is
provided, named revised, because it tries to fix some small problems
of the normal syntax.

Camlp4 can pretty print the normal Ocaml concrete syntax or the
revised one. It is therefore always possible to have a version of your
sources compilable by the Objective Caml compiler without
preprocessing.

%description -l pl.UTF-8
Camlp4 jest preprocesorem OCamla. Oferuje narzędzia do manipulowania
składnią (gramatyki) oraz możliwość modyfikowania oryginalnej składni
języka (cytowania, rozszerzenia).

Camlp4 potrafi analizować oryginalną składnię Ocamla lub dowolną inną
definiowalną przez użytkownika. Jako przykład podana jest alternatywna
składnia (revised syntax), która próbuje poprawić drobne problemy
występujące w składni oryginalnej.

Camlp4 umie ładnie formatować źródła zarówno w oryginalnej jak i
poprawionej składni OCamla. Potrafi także tłumaczyć programy z jednej
składni na drugą.

%package doc-html
Summary:	Objective Caml Preprocessor - HTML documentation 
Summary(pl.UTF-8):	Preprocesor OCamla - dokumentacja HTML 
Group:		Documentation

%description doc-html
Objective Caml Preprocessor - HTML documentation.

%description doc-html -l pl.UTF-8
Preprocesor OCamla - dokumentacja HTML.

%prep
%setup -q -n camlp4-%{main_ver}-%{subver} -a1 -a3

mkdir -p docs/html
mv camlp4-%{doc_ver}-manual.html docs/html/camlp4
cp %{SOURCE2} docs/camlp4.ps.gz
mv camlp4-%{doc_ver}-tutorial.html docs/html/camlp4-tutorial
cp %{SOURCE4} docs/camlp4-tutorial.ps.gz

%build
./configure

%{__make} %{?with_opt:all}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%attr(755,root,root) %{_bindir}/camlp4*
%attr(755,root,root) %{_bindir}/mkcamlp4
%{_libdir}/ocaml/camlp4

%files doc-html
%defattr(644,root,root,755)
%doc docs/html/camlp4*
