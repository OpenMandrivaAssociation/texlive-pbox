# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pbox
# catalog-date 2008-02-03 21:14:11 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-pbox
Version:	1.0
Release:	1
Summary:	A variable-width \parbox command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pbox
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines a command \pbox{<max width>}{<text>} which adjusts its
width to that of the enclosed text, up to the maximum width
given. The package also defines some associated length
commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pbox/pbox.sty
%doc %{_texmfdistdir}/doc/latex/pbox/AUTHORS
%doc %{_texmfdistdir}/doc/latex/pbox/COPYING
%doc %{_texmfdistdir}/doc/latex/pbox/ChangeLog
%doc %{_texmfdistdir}/doc/latex/pbox/INSTALL
%doc %{_texmfdistdir}/doc/latex/pbox/README
%doc %{_texmfdistdir}/doc/latex/pbox/pbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pbox/Makefile
%doc %{_texmfdistdir}/source/latex/pbox/pbox.drv
%doc %{_texmfdistdir}/source/latex/pbox/pbox.dtx
%doc %{_texmfdistdir}/source/latex/pbox/pbox.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
