import pytest
from src import Cell 

def test_density():
    cell = Cell(volume_mcm3=4000.0, weight_ng=4.0)
    assert cell.density() == 0.001

    another_cell = Cell(volume_mcm3=30000.0, weight_ng=850.0)
    density = another_cell.density()
    assert density == 0.028 and round(density, 3)


def test_mitosis():
    parent_cell = Cell(volume_mcm3=8000.0, weight_ng=2.0)
    parent_density = parent_cell.density()
    daughter_cell_a, daughter_cell_b = parent_cell.mitosis()
    
    assert not parent_cell.is_alive

    assert daughter_cell_a.volume_mcm3 == daughter_cell_b.volume_mcm3
    assert daughter_cell_a.volume_mcm3 == 4000.0
    
    assert daughter_cell_b.weight_ng == daughter_cell_a.weight_ng
    assert daughter_cell_b.weight_ng == 1.0

    assert daughter_cell_a.density() == parent_density


def test_consume():
    predator_cell = Cell(volume_mcm3=500.0, weight_ng=1.0)
    prey_cell = Cell(volume_mcm3=100.0, weight_ng=0.3)
    predator_cell.consume(prey_cell)

    assert predator_cell.volume_mcm3 == 600.0
    assert predator_cell.weight_ng == 1.3

    assert prey_cell.volume_mcm3 == 0.0
    assert prey_cell.weight_ng == 0.0
    assert not prey_cell.is_alive

