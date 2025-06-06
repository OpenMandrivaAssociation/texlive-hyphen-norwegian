Name:		texlive-hyphen-norwegian
Version:	73410
Release:	1
Summary:	Norwegian Bokmal and Nynorsk hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-norwegian.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-norwegian
%_texmf_language_def_d/hyphen-norwegian
%_texmf_language_lua_d/hyphen-norwegian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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
