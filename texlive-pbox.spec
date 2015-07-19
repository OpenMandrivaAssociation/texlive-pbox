# revision 24807
# category Package
# catalog-ctan /macros/latex/contrib/pbox
# catalog-date 2011-12-08 01:39:40 +0100
# catalog-license gpl2
# catalog-version 1.2
Name:		texlive-pbox
Version:	1.2
Release:	10
Summary:	A variable-width \parbox command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pbox
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 754726
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 743314
- texlive-pbox

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 739866
- texlive-pbox

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719211
- texlive-pbox
- texlive-pbox
- texlive-pbox
- texlive-pbox

