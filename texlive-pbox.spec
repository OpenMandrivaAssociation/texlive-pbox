Name:		texlive-pbox
Version:	24807
Release:	1
Summary:	A variable-width \parbox command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pbox
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a command \pbox{<max width>}{<text>} which adjusts its
width to that of the enclosed text, up to the maximum width
given. The package also defines some associated length
commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pbox/pbox.sty
%doc %{_texmfdistdir}/doc/latex/pbox/AUTHORS
%doc %{_texmfdistdir}/doc/latex/pbox/COPYING
%doc %{_texmfdistdir}/doc/latex/pbox/ChangeLog
%doc %{_texmfdistdir}/doc/latex/pbox/INSTALL
%doc %{_texmfdistdir}/doc/latex/pbox/Makefile
%doc %{_texmfdistdir}/doc/latex/pbox/README
%doc %{_texmfdistdir}/doc/latex/pbox/pbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pbox/pbox.drv
%doc %{_texmfdistdir}/source/latex/pbox/pbox.dtx
%doc %{_texmfdistdir}/source/latex/pbox/pbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
