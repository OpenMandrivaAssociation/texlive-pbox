%global tl_name pbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A variable-width \parbox command
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pbox
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a command \pbox{<max width>}{<text>} which adjusts its width to
that of the enclosed text, up to the maximum width given. The package
also defines some associated length commands.

