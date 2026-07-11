%global tl_name parsa
%global tl_revision 54840

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	A XeLaTeX package for theses and dissertations at Iranian Universities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/parsa
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parsa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parsa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for preparing dissertations and theses for Iranian
universities as fast and as efficiently as possible. The package depends
on xparse, fancyhdr, graphicx, multirow, float, and adjustbox.

