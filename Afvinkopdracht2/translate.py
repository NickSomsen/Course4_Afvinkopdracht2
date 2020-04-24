import re


def translate_sequence(seq):
    """ translate rna sequence to protein sequence

    Input: seq - string: "atgatgcctgac..."
    Output: protein sequence
    """
    seq = seq.lower()
    if re.search("[^atgcn]", seq):
        return "That's not a DNA sequence"
    else:
        seq_to_amino = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
                        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
                        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
                        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
                        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
                        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
                        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
                        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
                        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
                        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
                        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
                        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
                        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
                        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
                        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
                        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
                        }

        total_length = len(seq)
        protein = []

        start_triplet = 0  # start_triplet wordt gebruikt voor het slicen, en geeft start positie slicing aan
        end_triplet = 3  # end_triplet wordt gebruikt voor het slicen, en geeft eind positie aan
        try:
            if total_length % 3 == 0:  # wanneer de sequentie deelbaar is door 3, dan gebeurt het volgende:
                for i in range(total_length):
                    triplet = seq[start_triplet:end_triplet]  # triplet wordt gemaakt
                    protein.append(seq_to_amino[triplet])  # en toegevoegd aan een list
                    if end_triplet == total_length:  # wanneer het end_triplet gelijk is aan de totale lengte,
                        # dan is alles getransleerd, en moet de loop stoppen
                        break
                    else:  # is nog niet alles geweest, dan gebeurt de volgende slice
                        start_triplet += 3
                        end_triplet += 3
            else:
                # wanneer de sequentie niet deelbaar is door 3, dan gebeurt het volgende:
                for i in range(total_length):
                    if end_triplet > total_length:  # wanneer het end_triplet groter is dan het, dan stopt de
                        # translatie. Dit is om te voorkomen dat er nucleotiden getransleerd worden die géén tripletten
                        # vormen (dus 1 of 2 lang zijn)
                        break
                    else:
                        triplet = seq[start_triplet:end_triplet]
                        protein.append(seq_to_amino[triplet])
                        start_triplet += 3
                        end_triplet += 3

            protein = "".join(protein)
            return protein
        except KeyError:
            return "Unknown codon in sequence"
