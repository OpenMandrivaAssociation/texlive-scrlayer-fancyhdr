Name:		texlive-scrlayer-fancyhdr
Version:	63844
Release:	2
Summary:	Combining package fancyhdr with KOMA-Script's scrlayer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scrlayer-fancyhdr
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrlayer-fancyhdr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrlayer-fancyhdr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrlayer-fancyhdr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package uses KOMA-Script's scrlayer to redefine the
page styles of package fancyhdr. This allows the combination of
features of fancyhdr with features of scrlayer. Before
KOMA-Script v3.33 scrlayer-fancyhdr was part of KOMA-Script
itself.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/scrlayer-fancyhdr
%{_texmfdistdir}/tex/latex/scrlayer-fancyhdr
%doc %{_texmfdistdir}/doc/latex/scrlayer-fancyhdr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
