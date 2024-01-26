/*
 *  Copyright 2013,2015 DFKI GmbH Robotics Innovation Center
 *
 *  This file is part of the BOLeRo framework.
 *
 *  BOLeRo is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU Lesser General Public License
 *  as published by the Free Software Foundation, either version 3
 *  of the License, or (at your option) any later version.
 *
 *  BOLeRo is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *   You should have received a copy of the GNU Lesser General Public License
 *   along with bolero.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "Controller.h"


int main(int argc, char **argv) {
  bolero::Controller c;
  c.run();
  return 0;
}
