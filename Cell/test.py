import pytest
from src import Cell 

def test_A():
    cell = Cell(volume_mcm3=4000.0, weight_ng=4.0)
    assert cell.density() == 0.001

    another_cell = Cell(volume_mcm3=30000.0, weight_ng=850.0)
    assert another_cell.density() == 0.028


def test_B():
    parent_cell = Cell(volume_mcm3=8000.0, weight_ng=2.0)
    child_cell = parent_cell.mitosis()
    prior_density = parent_cell.density()

    assert parent_cell.volume_mcm3 == child_cell.volume_mcm3
    assert child_cell.weight_ng == parent_cell.weight_ng
    assert parent_cell.volume_mcm3 == 4000.0
    assert parent_cell.weight_ng == 1.0
    assert parent_cell.density() == prior_density

def test_C():
    predator_cell = Cell(volume_mcm3=500.0, weight_ng=1.0)
    prey_cell = Cell(volume_mcm3=100.0, weight_ng=0.3)
    predator_cell.consume(prey_cell)

    assert predator_cell.volume_mcm3 == 600.0
    assert predator_cell.weight_ng == 1.3

    assert prey_cell.volume_mcm3 == 0.0
    assert prey_cell.weight_ng == 0.0
    assert not prey_cell.is_alive

