Name:		texlive-parsa
Version:	54840
Release:	2
Summary:	A XeLaTeX package for theses and dissertations at Iranian Universities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parsa
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parsa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parsa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for preparing dissertations and theses for Iranian
universities as fast and as efficiently as possible. The
package depends on xparse, fancyhdr, graphicx, multirow, float,
and adjustbox.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/parsa
%doc %{_texmfdistdir}/doc/xelatex/parsa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
