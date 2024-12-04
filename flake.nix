{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { flake-utils, nixpkgs, ... }: 
  flake-utils.lib.eachDefaultSystem (system: let
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.docs = pkgs.mkShell {
      buildInputs = with pkgs.python312Packages; [
        pkgs.python312
        pip
        requests
        tqdm
      ];

      shellHook = ''
        PS1="(kattis)\n$PS1"
      '';
    };

    devShells.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        python312
        cargo
        rustc
        libgcc
        openjdk23
      ];

      shellHook = ''
        clear; zsh; exit
      '';
    };
  });
}
