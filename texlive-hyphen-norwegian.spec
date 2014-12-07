# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-norwegian
Version:	20120124
Release:	8
Summary:	Norwegian Bokmal and Nynorsk hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-norwegian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC
and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-norwegian
%_texmf_language_def_d/hyphen-norwegian
%_texmf_language_lua_d/hyphen-norwegian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-norwegian <<EOF
\%% from hyphen-norwegian:
bokmal loadhyph-nb.tex
=norwegian
=norsk
nynorsk loadhyph-nn.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-norwegian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-norwegian <<EOF
\%% from hyphen-norwegian:
\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-norwegian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-norwegian <<EOF
-- from hyphen-norwegian:
	['bokmal'] = {
		loader = 'loadhyph-nb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'norwegian', 'norsk' },
		patterns = 'hyph-nb.pat.txt',
		hyphenation = 'hyph-nb.hyp.txt',
	},
	['nynorsk'] = {
		loader = 'loadhyph-nn.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-nn.pat.txt',
		hyphenation = 'hyph-nn.hyp.txt',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120124-1
+ Revision: 767570
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 759930
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718672
- texlive-hyphen-norwegian
- texlive-hyphen-norwegian
- texlive-hyphen-norwegian
- texlive-hyphen-norwegian

