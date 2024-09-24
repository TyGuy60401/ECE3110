% This document class provides a simple memo for LaTeX users.
% It is based on article.cls and inherits most of the functionality
% that class.
% 
% Author: Rob Oakes, Copyright 2010.  Released under the LGPL, version 3.
% A copy of the LGPL can be found at http://www.gnu.org/licenses/lgpl.html

% Modified:  Eric Gibbons, Weber State University Department of Electrical
% and Computer Engineering.  

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{texMemo-gibbons}[2010/07/31 - Simple Memo Class, Including Logo]
%\RequirePackage{palatino}

% Load the Base Class
\LoadClassWithOptions{article}

% Begin Requirements
\RequirePackage{ifthen}
\RequirePackage{enumitem}

% Specialized memo Commands (To, From, Subject, Logo, Letterhead Address)

\def\@memostudent{\relax}
\newcommand{\memostudent}[1]{\gdef\@memostudent{#1}}

\def\@memocourse{\relax}
\newcommand{\memocourse}[1]{\gdef\@memocourse{#1}}

\def\@memosubject{\relax}
\newcommand{\memosubject}[1]{\gdef\@memosubject{#1}}

\def\@memodate{\relax}
\newcommand{\memodate}[1]{\gdef\@memodate{#1}}

\def\@memologo{\relax}
\newcommand{\logo}[1]{\gdef\@memologo{\protect #1}}

\def\@letterheadaddress{\relax}
\newcommand{\lhaddress}[1]{\gdef\@letterheadaddress{#1}}

% Custom Document Formatting
\newcommand\decorativeline[1][1pt]{
	\par\noindent%
	\rule[0.5ex]{\linewidth}{#1}\par
}

% Set the Paper Size and margins
\RequirePackage{geometry}
\geometry{top=1.0in,left=0.75in,right=0.75in,bottom=0.75in}
\RequirePackage[parfill]{parskip} % no indent on paragraphs


% Create the Letterhead and To/From Block

\renewcommand{\maketitle}{\makememotitle}
\newcommand\makememotitle{
	\ifthenelse{\equal{\@memologo}{\relax}}{}
	{ % Create With Logo
	\begin{minipage}[t]{1\columnwidth}%
		\begin{flushright}
			\vspace{-0.6in}
			\@memologo%
%			\vspace{-1.0in}
		\par\end{flushright}%
            \end{minipage}
            \vspace{-0.7in}
	}
	
	% To, From, Subject Block
	\begin{description}[itemsep=-0.7mm]
		\ifthenelse{\equal{\@memostudent}{\relax}}{}{\item [{Student:}] \@memostudent}
		\ifthenelse{\equal{\@memocourse}{\relax}}{}{\item [{Course:}] \@memocourse}
		\ifthenelse{\equal{\@memosubject}{\relax}}{}{\item [{Subject:}] \@memosubject}
		\ifthenelse{\equal{\@memodate}{\relax}}{}{\item [{Date:}] \@memodate}
	\end{description}
	\decorativeline\bigskip{}
}
